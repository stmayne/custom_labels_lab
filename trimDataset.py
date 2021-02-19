#!/usr/bin/env python
# coding: utf-8

'''
SPDX-FileCopyrightText: Copyright Amazon.com Inc. or its affiliates.

SPDX-License-Identifier: MIT
'''

import os
import random
import shutil


random.seed(12345)
folders = os.listdir('Images/')
class_list = ['Walker_hound', 'briard', 'Australian_terrier', 'Chesapeake_Bay_retriever', 'Norwich_terrier', 'Chihuahua', 'affenpinscher', 'Irish_water_spaniel', 'silky_terrier', 'cocker_spaniel', 'Leonberg', 'basenji', 'American_Staffordshire_terrier', 'English_setter', 'dingo', 'Pekinese', 'Great_Pyrenees', 'malinois', 'Greater_Swiss_Mountain_dog', 'German_short-haired_pointer', 'Afghan_hound', 'collie', 'pug', 'Welsh_springer_spaniel', 'soft-coated_wheaten_terrier', 'Airedale', 'keeshond', 'EntleBucher', 'Border_collie', 'giant_schnauzer', 'Rhodesian_ridgeback', 'standard_poodle', 'Great_Dane', 'Irish_terrier', 'black-and-tan_coonhound', 'Tibetan_terrier', 'Scotch_terrier', 'Dandie_Dinmont', 'curly-coated_retriever', 'redbone', 'Saint_Bernard', 'dhole', 'Gordon_setter', 'Eskimo_dog', 'toy_poodle', 'African_hunting_dog', 'Mexican_hairless', 'Yorkshire_terrier', 'Irish_wolfhound', 'Scottish_deerhound', 'Doberman', 'Newfoundland', 'Appenzeller', 'schipperke', 'Border_terrier', 'cairn', 'malamute', 'Rottweiler', 'Japanese_spaniel', 'kuvasz', 'beagle', 'Staffordshire_bullterrier', 'Cardigan', 'whippet', 'standard_schnauzer', 'Brabancon_griffon', 'chow', 'West_Highland_white_terrier', 'Pembroke', 'Boston_bull', 'golden_retriever', 'French_bulldog', 'komondor', 'bull_mastiff', 'German_shepherd', 'English_springer', 'Kerry_blue_terrier', 'kelpie', 'Maltese_dog', 'miniature_schnauzer', 'wire-haired_fox_terrier', 'bluetick', 'basset', 'Samoyed', 'English_foxhound', 'Lhasa', 'Sealyham_terrier', 'Norwegian_elkhound', 'Shih-Tzu', 'Siberian_husky', 'Bedlington_terrier', 'borzoi', 'Italian_greyhound', 'bloodhound', 'Bernese_mountain_dog', 'Blenheim_spaniel', 'Irish_setter', 'groenendael', 'Sussex_spaniel', 'Shetland_sheepdog', 'toy_terrier', 'miniature_pinscher', 'miniature_poodle', 'flat-coated_retriever', 'otterhound', 'Old_English_sheepdog', 'folder[10:]', 'Ibizan_hound', 'boxer', 'Brittany_spaniel', 'clumber', 'Bouvier_des_Flandres', 'Saluki', 'Labrador_retriever', 'Tibetan_mastiff', 'vizsla', 'Norfolk_terrier', 'papillon', 'Weimaraner', 'Pomeranian', 'Lakeland_terrier']
random_classes = random.sample(folders, 20)

for folder in folders:
    if folder in random_classes:
        os.mkdir(f'Images/{folder[10:]}/')
        if 'n02' in folder:
            for image in os.listdir(f'Images/{folder}'):
                try:
                    os.rename(f'Images/{folder}/{image}', f'Images/{folder[10:]}/{image}')
                except AttributeError:
                    True
for folder in folders:
    if 'n02' in folder:
        shutil.rmtree(f'Images/{folder}')
