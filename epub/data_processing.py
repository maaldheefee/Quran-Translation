import csv
from collections import defaultdict


def load_quran_data(quran_data_file):
    with open(quran_data_file, "r", encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def load_translation_data(translation_file):
    translations = {}
    with open(translation_file, "r", encoding='utf-8') as file:
        for line in file:
            try:
                sura_no, aya_no, translation = line.strip().split("|")
                translations[(int(sura_no), int(aya_no))] = translation
            except ValueError:
                break
    return translations


def merge_data(quran_data, translation_data):
    for row in quran_data:
        key = (int(row["sura_no"]), int(row["aya_no"]))
        if key in translation_data:
            row["translation"] = translation_data[key]
    return quran_data


def group_by_surah(data):
    surahs = defaultdict(list)
    for row in data:
        surahs[row["sura_no"]].append(row)
    return surahs


def get_surah_data(quran_data_file, translation_data_file):
    """
    quran_data_file: csv file from https://qurancomplex.gov.sa/techquran/dev/
    translation_data_file: txt file in Tanzil's format
    """
    quran_data = load_quran_data(quran_data_file)
    translation_data = load_translation_data(translation_data_file)
    merged_data = merge_data(quran_data, translation_data)
    return group_by_surah(merged_data)
