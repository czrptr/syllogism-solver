#!/usr/bin/env python3

# run check
if __name__ != "__main__":
	print("sylo.py: this script is supposed to be run as a program")
	exit(1)

# implementation
from typing import *
import sys, inflect, subprocess, os, re

CLIPS_BASE = ''
with open('base.clp', 'r') as f:
	CLIPS_BASE = f.read()

engine = inflect.engine()
all_premise = r'all\s+(\w+)\s+are\s+(\w+)\.?'
no_premise = r'no\s+(\w+)\s+(are|is)\s+(\w+)\.?'
some_premise = r'some\s+(\w+)\s+are\s+(\w+)\.?'
someno_premise = r'some\s+(\w+)\s+are\s+not\s+(\w+)\.?'
specific_premise = r'(\w+(\s+\w+)*)\s+(are|is)\s+(\w+)\.?'
specificno_premise = r'(\w+(\s+\w+)*)\s+(are|is)\s+not\s+(\w+)\.?'

def singular(noun: str) -> str:
	aux = engine.singular_noun(noun)
	return aux if aux else noun

def format_fact(premise: str) -> str:
	aux_premise = premise.lower().replace(' a ', ' ').replace(' an ', ' ').replace(' the ', ' ')
	match = re.match(all_premise, aux_premise)
	if match:
		return f'ALL {singular(match.group(1))} {singular(match.group(2))}'

	match = re.match(no_premise, aux_premise)
	if match:
		return f'NO {singular(match.group(1))} {singular(match.group(3))}'

	match = re.match(someno_premise, aux_premise)
	if match:
		return f'SOMENO {singular(match.group(1))} {singular(match.group(2))}'

	match = re.match(some_premise, aux_premise)
	if match:
		return f'SOME {singular(match.group(1))} {singular(match.group(2))}'

	match = re.match(specificno_premise, aux_premise)
	if match:
		return f'SPECIFICNO {match.group(1).replace(" ", "_")} {singular(match.group(4))}'

	match = re.match(specific_premise, aux_premise)
	if match:
		return f'SPECIFIC {match.group(1).replace(" ", "_")} {singular(match.group(4))}'

def premises_to_facts(premises: List[str]) -> str:
	facts = '(deffacts premises\n'
	for premise in premises:
		facts += f'\t({format_fact(premise)})\n'
	facts += ')\n\n'
	return facts

# input
INTERACT = False

premises: List[str] = []
conclusion = ''

if len(sys.argv) == 2:
	with open(sys.argv[1], 'r') as f:
		try:
			premises_count = int(f.readline().strip())
		except:
			print(f'{sys.argv[1]}:1: expected the number of premises')
			exit(1)
		for i in range(premises_count):
			premises += [f.readline().strip()]
		conclusion = f.readline().strip()
else:
	INTERACT = True
	try:
		premises_count = int(input('How many premises? '))
	except:
		print('sylo.py: expected the number of premises')
		exit(1)

	for i in range(premises_count):
		premises += [input(f'P{i + 1}: ')]
	conclusion = input('C: ')

# execute
with open('aux.clp', 'w') as f:
	f.write(premises_to_facts(premises) + CLIPS_BASE)

inferred: List[str] = subprocess.check_output(['clips', '-f2', 'aux.clp']).decode('utf8').split('\n')[1:-2]
os.remove('aux.clp')
inferred = [re.match(r'f-\d+\s+\((.+)\)', fact).group(1) for fact in inferred]

# output
if INTERACT:
	print()
else:
	for i, premise in enumerate(premises):
		print(f'P{i + 1}: {premise}')
	print(f'C: {conclusion}\n')

if format_fact(conclusion) in inferred:
	print('The syllogism is correct.\nThe conclusion follows from the premises.')
else:
	print('The syllogism is incorrect.\nThe conclusion does not follow from the premises.')