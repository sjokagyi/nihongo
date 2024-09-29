ROMAJI_TO_HIRAGANA = {
    'a': 'あ', 'i': 'い', 'u': 'う', 'e': 'え', 'o': 'お',
    'ka': 'か', 'ki': 'き', 'ku': 'く', 'ke': 'け', 'ko': 'こ',
    'kya': 'きゃ', 'kyu': 'きゅ', 'kyo': 'きょ',
    'sa': 'さ', 'shi': 'し', 'su': 'す', 'se': 'せ', 'so': 'そ',
    'sha': 'しゃ', 'shu': 'しゅ', 'sho': 'しょ',
    'ta': 'た', 'chi': 'ち', 'tsu': 'つ', 'te': 'て', 'to': 'と',
    'cha': 'ちゃ', 'chu': 'ちゅ', 'cho': 'ちょ',
    'na': 'な', 'ni': 'に', 'nu': 'ぬ', 'ne': 'ね', 'no': 'の',
    'nya': 'にゃ', 'nyu': 'にゅ', 'nyo': 'にょ',
    'ha': 'は', 'hi': 'ひ', 'fu': 'ふ', 'he': 'へ', 'ho': 'ほ',
    'hya': 'ひゃ', 'hyu': 'ひゅ', 'hyo': 'ひょ',
    'ma': 'ま', 'mi': 'み', 'mu': 'む', 'me': 'め', 'mo': 'も',
    'mya': 'みゃ', 'myu': 'みゅ', 'myo': 'みょ',
    'ra': 'ら', 'ri': 'り', 'ru': 'る', 're': 'れ', 'ro': 'ろ',
    'rya': 'りゃ', 'ryu': 'りゅ', 'ryo': 'りょ',
    'wa': 'わ', 'wo': 'を', 'n': 'ん',
    'ga': 'が', 'gi': 'ぎ', 'gu': 'ぐ', 'ge': 'げ', 'go': 'ご',
    'gya': 'ぎゃ', 'gyu': 'ぎゅ', 'gyo': 'ぎょ',
    'za': 'ざ', 'ji': 'じ', 'zu': 'ず', 'ze': 'ぜ', 'zo': 'ぞ',
    'ja': 'じゃ', 'ju': 'じゅ', 'jo': 'じょ',
    'da': 'だ', 'ji': 'ぢ', 'zu': 'づ', 'de': 'で', 'do': 'ど',
    'ba': 'ば', 'bi': 'び', 'bu': 'ぶ', 'be': 'べ', 'bo': 'ぼ',
    'bya': 'びゃ', 'byu': 'びゅ', 'byo': 'びょ',
    'pa': 'ぱ', 'pi': 'ぴ', 'pu': 'ぷ', 'pe': 'ぺ', 'po': 'ぽ',
    'pya': 'ぴゃ', 'pyu': 'ぴゅ', 'pyo': 'ぴょ',
    'nn': 'ん',
    'ou': 'おう',  # Handle long vowel sounds in words like "sayonara"
}

ROMAJI_TO_KATAKANA = {
    'a': 'ア', 'i': 'イ', 'u': 'ウ', 'e': 'エ', 'o': 'オ',
    'ka': 'カ', 'ki': 'キ', 'ku': 'ク', 'ke': 'ケ', 'ko': 'コ',
    'kya': 'キャ', 'kyu': 'キュ', 'kyo': 'キョ',
    'sa': 'サ', 'shi': 'シ', 'su': 'ス', 'se': 'セ', 'so': 'ソ',
    'sha': 'シャ', 'shu': 'シュ', 'sho': 'ショ',
    'ta': 'タ', 'chi': 'チ', 'tsu': 'ツ', 'te': 'テ', 'to': 'ト',
    'cha': 'チャ', 'chu': 'チュ', 'cho': 'チョ',
    'na': 'ナ', 'ni': 'ニ', 'nu': 'ヌ', 'ne': 'ネ', 'no': 'ノ',
    'nya': 'ニャ', 'nyu': 'ニュ', 'nyo': 'ニョ',
    'ha': 'ハ', 'hi': 'ヒ', 'fu': 'フ', 'he': 'ヘ', 'ho': 'ホ',
    'hya': 'ヒャ', 'hyu': 'ヒュ', 'hyo': 'ヒョ',
    'ma': 'マ', 'mi': 'ミ', 'mu': 'ム', 'me': 'メ', 'mo': 'モ',
    'mya': 'ミャ', 'myu': 'ミュ', 'myo': 'ミョ',
    'ra': 'ラ', 'ri': 'リ', 'ru': 'ル', 're': 'レ', 'ro': 'ロ',
    'wa': 'ワ', 'wo': 'ヲ', 'n': 'ン',
    'nn': 'ン',  # Handle double 'n' for nasal sound
    'ou': 'オウ',  # Handle 'ou' for long vowels
    'ga': 'ガ', 'gi': 'ギ', 'gu': 'グ', 'ge': 'ゲ', 'go': 'ゴ',
    'gya': 'ギャ', 'gyu': 'ギュ', 'gyo': 'ギョ',
    'za': 'ザ', 'ji': 'ジ', 'zu': 'ズ', 'ze': 'ゼ', 'zo': 'ゾ',
    'da': 'ダ', 'ji': 'ヂ', 'zu': 'ヅ', 'de': 'デ', 'do': 'ド',
    'ba': 'バ', 'bi': 'ビ', 'bu': 'ブ', 'be': 'ベ', 'bo': 'ボ',
    'pa': 'パ', 'pi': 'ピ', 'pu': 'プ', 'pe': 'ペ', 'po': 'ポ',
    'kya': 'キャ', 'kyu': 'キュ', 'kyo': 'キョ',
    'ja': 'ジャ', 'ju': 'ジュ', 'jo': 'ジョ',
    'bya': 'ビャ', 'byu': 'ビュ', 'byo': 'ビョ',
    'pya': 'ピャ', 'pyu': 'ピュ', 'pyo': 'ピョ',
    'ー': 'ー',  # Long vowel marker
    'ッ': 'ッ',  # Sokuon for geminate consonants (double consonants)
}

def translate_to_hiragana(romaji):
    return _translate(romaji, ROMAJI_TO_HIRAGANA)

def translate_to_katakana(romaji):
    return _translate(romaji, ROMAJI_TO_KATAKANA)



def _translate(romaji, conversion_map):
    translation = ""
    romaji = romaji.lower()  # Convert to lowercase
    i = 0
    while i < len(romaji):
        if romaji[i] == ' ':  # Preserve spaces
            translation += ' '
            i += 1
        elif romaji[i] == '\n':  # Preserve new lines
            translation += '\n'
            i += 1
        elif i + 1 < len(romaji) and romaji[i:i + 2] == 'nn':
            translation += conversion_map.get('nn', 'ん')  # Handle 'nn' as ん
            i += 2
        elif i + 2 <= len(romaji) and romaji[i:i + 2] == 'ou':  # Handle long vowel sounds like "ou"
            translation += conversion_map.get('ou', 'おう')
            i += 2
        elif i + 2 <= len(romaji) and romaji[i:i + 2] in conversion_map:
            translation += conversion_map[romaji[i:i + 2]]  # Handle 2-letter mappings like "shi", "kya", etc.
            i += 2
        elif i + 1 < len(romaji) and romaji[i] == romaji[i + 1] and romaji[i] in 'kstnhmyrwgbzpd':
            translation += conversion_map.get('ッ', 'っ')  # Handle gemination (double consonants)
            i += 1
        elif romaji[i] in conversion_map:
            translation += conversion_map[romaji[i]]  # Handle single letters
            i += 1
        else:
            i += 1  # Skip unknown characters
    return translation




HIRAGANA_TO_ROMAJI = {v: k for k, v in ROMAJI_TO_HIRAGANA.items()}
KATAKANA_TO_ROMAJI = {v: k for k, v in ROMAJI_TO_KATAKANA.items()}

def hiragana_to_romaji(hiragana):
    return _reverse_translate(hiragana, HIRAGANA_TO_ROMAJI)

def katakana_to_romaji(katakana):
    return _reverse_translate(katakana, KATAKANA_TO_ROMAJI)

def _reverse_translate(text, reverse_map):
    translation = ""
    i = 0
    while i < len(text):
        if text[i] == ' ':  # Preserve spaces
            translation += ' '
            i += 1
        elif text[i] == '\n':  # Preserve new lines
            translation += '\n'
            i += 1
        elif text[i] == 'ッ':  # Handle gemination for Katakana
            if i + 1 < len(text):
                translation += reverse_map.get(text[i + 1], '')[0] * 2  # Double consonants
                i += 1
            i += 1
        elif text[i] == 'っ':  # Handle gemination for Hiragana
            if i + 1 < len(text):
                translation += reverse_map.get(text[i + 1], '')[0] * 2  # Double consonants
                i += 1
            i += 1
        elif i + 2 <= len(text) and text[i:i + 2] in reverse_map:
            translation += reverse_map[text[i:i + 2]]
            i += 2
        elif text[i] in reverse_map:
            translation += reverse_map[text[i]]
            i += 1
        else:
            i += 1  # Skip unknown characters
    return translation