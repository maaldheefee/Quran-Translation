import re

arabic_to_hindi = str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")


def format_aya_text(aya_text, aya_no):
    aya_text = re.sub(
        r"(۞|۩)",
        r"<span class='symbol'>\1</span>",
        aya_text,
        flags=re.UNICODE,
    )
    aya_text = re.sub(
        r"(\u06D6|\u06DB)",
        r"<span class='waqf'>\1</span>",
        aya_text,
        flags=re.UNICODE,
    )
    aya_text += f"\xa0<span class='ayah_num_ar'>\u202e{aya_no.translate(arabic_to_hindi)}\u202C</span>"
    return aya_text


def format_trans_text(translation: str):
    return translation.replace("\t", "<br>")  # Bring notes to a new line
