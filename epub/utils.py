import itertools


def merge_multi_ayah_translations(aya_list, trans_list, separator=" "):
    """
    Deduplicate aya_list and merges corresponding trans_list.

    Args:
        aya_list: A list of strings to be deduplicated.
        trans_list: A list of strings of the same length as ayah_texts,
                    containing corresponding values to be merged.
        separator: The string to use as a separator when merging trans_texts.
                    Defaults to a space.

    Returns:
        A list of tuples, where each tuple contains:
            - The merged ayahs, separated by the specified separator.
            - The unique translation.

    Example:
        ayah_texts = ["apple", "banana", "cherry", "durian", "elderberry", "fig", "guava"]
        trans_texts = ["A", "B", "B", "C", "C", "C", "D"]

        result = merge_multi_ayah_translations(ayah_texts, trans_texts, separator="-")
        print(result)  # Output: [('apple', 'A'), ('banana-cherry', 'B'), ('durian-elderberry-fig', 'C'), ('guava', 'D')]
    """

    grouped = itertools.groupby(zip(trans_list, aya_list), key=lambda x: x[0])
    return [(separator.join(text for _, text in group), key) for key, group in grouped]

# from collections import OrderedDict
#
# def merge_multi_ayah_translations(ayah_texts, trans_texts, separator=" "):
#   """
#   Deduplicates the second list by merging records in the first list.
#
#   Args:
#     ayah_texts: A list of strings.
#     trans_texts: A list of strings of the same length as ayah_texts.
#     separator: The string to use as a separator when joining the ayah_texts.
#                 Defaults to a space.
#
#   Returns:
#     A tuple of two lists:
#       - The deduplicated ayah_texts list.
#       - The deduplicated trans_texts list.
#   """
#
#   mapping = OrderedDict()
#   for i, (ayah_text, trans_text) in enumerate(zip(ayah_texts, trans_texts)):
#     if trans_text not in mapping:
#       mapping[trans_text] = []
#     mapping[trans_text].append(ayah_text)
#
#   deduplicated_ayah_texts = []
#   deduplicated_trans_texts = []
#   for text, texts in mapping.items():
#     deduplicated_ayah_texts.append(separator.join(texts))  # Use the separator here
#     deduplicated_trans_texts.append(text)
#
#   return zip(deduplicated_ayah_texts, deduplicated_trans_texts)
