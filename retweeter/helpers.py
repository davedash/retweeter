from langdetect import detect_langs, DetectorFactory

DetectorFactory.seed = 0


def probably_english(text):
  langs = detect_langs(text)
  if langs[0].lang == 'en' and len(langs) == 1:
    return True
  return False
