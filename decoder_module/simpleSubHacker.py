# Simple Substitution Cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)

import os, re, copy, pprint, pyperclip, simpleSubCipher, makeWordPatterns

if not os.path.exists('wordPatterns.py'):
    makeWordPatterns.main() # create the wordPatterns.py file
import wordPatterns

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nonLettersOrSpacePattern = re.compile('[^A-Z\s]')

def main():
#This is what is being decrypted
    message = """“vu’m y ktoervyz ykkyzyuem,” myvw uqt lxxvotz ul uqt uzyatrrtz, pynvjp svuq y otzuyvj ywhvzyuvlj yu uqt wtavot, svuq sqvoq qt sym, lx olezmt, uqlzlepqrf xyhvrvyz. vu ykktyztw uqyu uqt uzyatrrtz qyw ztmkljwtw ul uqt vjavuyuvlj lx uqt olhhyjwyju ljrf leu lx klrvutjtmm, sqtj qt qyw cttj ymbtw ul yuutjw uqt tdtoeuvlj lx y mlrwvtz oljwthjtw xlz wvmlctfvjp yjw vjmeruvjp qvm mektzvlz. lx olezmt, vjutztmu vj uqt tdtoeuvlj sym jlu atzf qvpq tatj vj uqt ktjyr olrljf vumtrx. yu rtymu, qtzt vj uqt mhyrr, wttk, myjwf ayrrtf, orlmtw vj lj yrr mvwtm cf cyzztj mrlktm, ykyzu xzlh uqt lxxvotz yjw uqt uzyatrrtz uqtzt stzt kztmtju ljrf uqt oljwthjtw, y ayoyju-rllbvjp hyj svuq y czlyw hleuq yjw wvrykvwyutw qyvz yjw xyot, yjw uqt mlrwvtz, sql qtrw uqt qtyaf oqyvj ul sqvoq stzt oljjtoutw uqt mhyrr oqyvjm sqvoq clejw uqt oljwthjtw hyj cf qvm xttu yjw szvmu cljtm, ym strr ym cf qvm jtob, yjw sqvoq stzt yrml rvjbtw ul tyoq luqtz cf oljjtouvjp oqyvjm. uqt oljwthjtw hyj, vjovwtjuyrrf, qyw yj tdkztmmvlj lx meoq wlp-rvbt ztmvpjyuvlj uqyu vu rllbtw ym vx ljt olerw mtu qvh xztt ul zlyh yzlejw uqt mrlktm yjw slerw ljrf qyat ul sqvmurt yu uqt muyzu lx uqt tdtoeuvlj xlz qvh ul ztuezj.
uqt uzyatrrtz qyw rvuurt vjutztmu vj uqt ykkyzyuem yjw syrbtw cyob yjw xlzuq ctqvjw uqt oljwthjtw hyj, yrhlmu avmvcrf vjwvxxtztju, sqvrt uqt lxxvotz ullb oyzt lx uqt xvjyr kztkyzyuvljm. mlhtuvhtm qt ozysrtw ejwtz uqt ykkyzyuem, sqvoq sym cevru wttk vjul uqt tyzuq, yjw mlhtuvhtm qt orvhctw ek y rywwtz ul vjmktou uqt ekktz kyzum. uqtmt stzt ztyrrf ilcm sqvoq olerw qyat cttj rtxu ul y htoqyjvo, ceu uqt lxxvotz oyzzvtw uqth leu svuq pztyu tjuqemvymh, hyfct ctoyemt qt sym kyzuvoeryzrf xljw lx uqvm ykkyzyuem lz hyfct ctoyemt uqtzt sym mlht luqtz ztymlj sqf ljt olerw jlu uzemu uqt slzb ul yjfljt trmt. “vu’m yrr ztywf jls!” qt xvjyrrf ozvtw yjw orvhctw cyob wlsj uqt rywwtz. qt sym ejemeyrrf uvztw, cztyuqvjp svuq qvm hleuq svwt lktj, yjw qt qyw kemqtw usl xvjt rywf’m qyjwbtzoqvtxm ejwtz uqt olrryz lx qvm ejvxlzh.
“uqtmt ejvxlzhm yzt ztyrrf ull qtyaf xlz uqt uzlkvom,” uqt uzyatrrtz myvw, vjmutyw lx ymbvjp mlht getmuvljm ycleu uqt ykkyzyuem, ym uqt lxxvotz qyw tdktoutw. “uqyu’m uzet,” myvw uqt lxxvotz. qt symqtw uqt lvr yjw pztymt xzlh qvm wvzuf qyjwm vj y ceobtu lx syutz muyjwvjp ztywf, “ceu uqtf htyj qlht, yjw st wlj’u syju ul rlmt lez qlhtryjw.” “jls, qyat y rllb yu uqvm ykkyzyuem,” qt ywwtw vhhtwvyutrf, wzfvjp qvm qyjwm svuq y ulstr yjw klvjuvjp ul uqt wtavot. “ek ul uqvm klvju v qyw ul wl mlht slzb cf qyjw, ceu xzlh jls lj uqt ykkyzyuem mqlerw slzb tjuvztrf lj vum lsj.” uqt uzyatrrtz jlwwtw yjw xlrrlstw uqt lxxvotz. uqt ryuutz uzvtw ul kzlutou qvhmtrx ypyvjmu yrr tatjueyrvuvtm cf myfvjp, “lx olezmt, cztybwlsjm wl qykktj. v ztyrrf qlkt jljt svrr looez ulwyf, ceu st hemu ct kztkyztw xlz vu. uqt ykkyzyuem vm mekklmtw ul bttk plvjp xlz ustrat qlezm svuqleu vjutzzekuvlj.'"""

    # Determine the possible valid ciphertext translations.
    #print('Hacking...')
    letterMapping = hackSimpleSub(message)

    # Display the results to the user.
    #print('Mapping:')
    pprint.pprint(letterMapping)
    #print()
    #print('Original ciphertext:')
    #print(message)
    #print()
    #print('Copying hacked message to clipboard:')
    hackedMessage = decryptWithCipherletterMapping(message, letterMapping)
    pyperclip.copy(hackedMessage)
    print(hackedMessage)
    return hackedMessage

def getBlankCipherletterMapping():
    # Returns a dictionary value that is a blank cipherletter mapping.
    return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}


def addLettersToMapping(letterMapping, cipherword, candidate):
    # The letterMapping parameter is a "cipherletter mapping" dictionary
    # value that the return value of this function starts as a copy of.
    # The cipherword parameter is a string value of the ciphertext word.
    # The candidate parameter is a possible English word that the
    # cipherword could decrypt to.

    # This function adds the letters of the candidate as potential
    # decryption letters for the cipherletters in the cipherletter
    # mapping.

    letterMapping = copy.deepcopy(letterMapping)
    for i in range(len(cipherword)):
        if candidate[i] not in letterMapping[cipherword[i]]:
            letterMapping[cipherword[i]].append(candidate[i])
    return letterMapping


def intersectMappings(mapA, mapB):
    # To intersect two maps, create a blank map, and then add only the
    # potential decryption letters if they exist in BOTH maps.
    intersectedMapping = getBlankCipherletterMapping()
    for letter in LETTERS:

        # An empty list means "any letter is possible". In this case just
        # copy the other map entirely.
        if mapA[letter] == []:
            intersectedMapping[letter] = copy.deepcopy(mapB[letter])
        elif mapB[letter] == []:
            intersectedMapping[letter] = copy.deepcopy(mapA[letter])
        else:
            # If a letter in mapA[letter] exists in mapB[letter], add
            # that letter to intersectedMapping[letter].
            for mappedLetter in mapA[letter]:
                if mappedLetter in mapB[letter]:
                    intersectedMapping[letter].append(mappedLetter)

    return intersectedMapping


def removeSolvedLettersFromMapping(letterMapping):
    # Cipher letters in the mapping that map to only one letter are
    # "solved" and can be removed from the other letters.
    # For example, if 'A' maps to potential letters ['M', 'N'], and 'B'
    # maps to ['N'], then we know that 'B' must map to 'N', so we can
    # remove 'N' from the list of what 'A' could map to. So 'A' then maps
    # to ['M']. Note that now that 'A' maps to only one letter, we can
    # remove 'M' from the list of letters for every other
    # letter. (This is why there is a loop that keeps reducing the map.)
    letterMapping = copy.deepcopy(letterMapping)
    loopAgain = True
    while loopAgain:
        # First assume that we will not loop again:
        loopAgain = False

        # solvedLetters will be a list of uppercase letters that have one
        # and only one possible mapping in letterMapping
        solvedLetters = []
        for cipherletter in LETTERS:
            if len(letterMapping[cipherletter]) == 1:
                solvedLetters.append(letterMapping[cipherletter][0])

        # If a letter is solved, than it cannot possibly be a potential
        # decryption letter for a different ciphertext letter, so we
        # should remove it from those other lists.
        for cipherletter in LETTERS:
            for s in solvedLetters:
                if len(letterMapping[cipherletter]) != 1 and s in letterMapping[cipherletter]:
                    letterMapping[cipherletter].remove(s)
                    if len(letterMapping[cipherletter]) == 1:
                        # A new letter is now solved, so loop again.
                        loopAgain = True
    return letterMapping


def hackSimpleSub(message):
    intersectedMap = getBlankCipherletterMapping()
    cipherwordList = nonLettersOrSpacePattern.sub('', message.upper()).split()
    for cipherword in cipherwordList:
        # Get a new cipherletter mapping for each ciphertext word.
        newMap = getBlankCipherletterMapping()

        wordPattern = makeWordPatterns.getWordPattern(cipherword)
        if wordPattern not in wordPatterns.allPatterns:
            continue # This word was not in our dictionary, so continue.

        # Add the letters of each candidate to the mapping.
        for candidate in wordPatterns.allPatterns[wordPattern]:
            newMap = addLettersToMapping(newMap, cipherword, candidate)

        # Intersect the new mapping with the existing intersected mapping.
        intersectedMap = intersectMappings(intersectedMap, newMap)

    # Remove any solved letters from the other lists.
    return removeSolvedLettersFromMapping(intersectedMap)


def decryptWithCipherletterMapping(ciphertext, letterMapping):
    # Return a string of the ciphertext decrypted with the letter mapping,
    # with any ambiguous decrypted letters replaced with an _ underscore.

    # First create a simple sub key from the letterMapping mapping.
    key = ['x'] * len(LETTERS)
    for cipherletter in LETTERS:
        if len(letterMapping[cipherletter]) == 1:
            # If there's only one letter, add it to the key.
            keyIndex = LETTERS.find(letterMapping[cipherletter][0])
            key[keyIndex] = cipherletter
        else:
            ciphertext = ciphertext.replace(cipherletter.lower(), '_')
            ciphertext = ciphertext.replace(cipherletter.upper(), '_')
    key = ''.join(key)

    # With the key we've created, decrypt the ciphertext.
    return simpleSubCipher.decryptMessage(key, ciphertext)


if __name__ == '__main__':
    main()