# Simple Substitution Cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)

import os, re, copy, pprint, pyperclip, simpleSubCipher, makeWordPatterns

if not os.path.exists('wordPatterns.py'):
    makeWordPatterns.main() # create the wordPatterns.py file
import wordPatterns

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÜÑÍÓÉÁÚÇÈÏÛÔÎËÊÄÂ'
nonLettersOrSpacePattern = re.compile('[^A-Â\s]')

def main():
#This is what is being decrypted
    message = """tcg ldn pd qkudhvc ytge df eg fdcfgykóc itd qdug eg ptdhmd. cv df drgymgpdcmd qvevh... df eg gtfdcykg qd dfadhgcng.
gcqhéf adcdmhó dc de kcxófakmv ygeeduóc, itdhíg hdytadhgh ft wgeóc adhqkqv. pkhó ge svcqv aghg qklkfgh tc shkó pthv, atdf gitde ygckcv cv eedlgwg g ckcotcg aghmd, mgc fvev dhg eg dcdpkfmgq dcmhd qvf dqkskykvf.
geov ed eegpó eg gmdcykóc, fd gahvrkpó ge fvekmghkv pthv aghg gqpkhgh yvc gfvpwhv de dfwvnv qd tcg fketdmg sdpdckcg. g adfgh qd fdh kcyvpaedmg fd kcmtíg adhsdyykóc b wdeedng.
agfghvc geotcvf qígf. gcqhéf hdyvhqó eg fketdmg qde pthv b yvhhkó xgykg deeg ahdfv qd eg ythkvfkqgq.
gxvhg eg vwhg yvpdcngwg g mdcdh hvfmhv. mhgnvf háakqvf itd qgwgc akfmgf qd qtenthg, ftf pgcvf mgpwkéc dfmgwgc qdskckqgf.
avyv g avyv eg akcmthg glgcngwg. de ptyxgyxv fd gahdfthgwg ygqg mghqd xgfmg de ygeeduóc. eg kcyvpaedmg ptudh mhgcfpkmíg fdcmkpkdcmvf qdfqd ft lkldng qd yvevhdf. gcqhéf fd fdcmíg gwhgngqv avh deevf. dhg mgc qteyd! mgc wvckmg!
gitdeeg mghqd agfó xvhgf qkfshtmgcqv qd eg gcóckpg fdñvhg. yhdbó itd eg akcmthg geygcnó ft méhpkcv. ft drahdfkóc dhg lklg b ftf vuvf fvchdígc g adfgh qd itd eg hvqdgwg tc gthg pdegcyóekyg.
pghyxó mhkfmd, yvcmgokgqv avh eg qgpg itd qteydpdcmd fd mgagwg evf egwkvf yvc evf qdqvf qd eg pgcv.
gitdeeg cvyxd qdfadhmó fvwhdfgemgqv. qácqvfd ytdcmg qd ev dcmhgqg itd dfmgwg eg cvyxd, dfygaó qd eg ygfg g xthmgqkeegf aghg yvhhdh ge ygeeduóc. ge aíd qd eg akcmthg, dc de ftdev, bgyíg tc gcykgcv! cv hdfakhgwg, dc ft atñv gsdhhgwg tc akcyde b dfmgwg hvqdgqv qd hdmvhykqvf hdykakdcmdf qd akcmthg. gcqhéf genó eg pkhgqg aghg gfvpwhghfd gcmd de hvfmhv qd eg qgpg. egf úemkpgf akcydegqgf qde gcykgcv qkwtughvc eáohkpgf dc gitdeeg dckopámkyg sgn. ge ckñv ev kclgqkdhvc egf ogcgf qd eevhgh. adhv fd hdatfv, ekpakgcqv egf eáohkpgf qd shdfyg akcmthg yvc eg pgcog qd ft akugpg. “cv eevhdf, bg cv mkdcdf avh itd. gxvhg ée dfmá yvc mkov” yvcfveó pkhgcqv ge gcykgcv.
ugpáf lvelkó ge ygeeduóc. páf avh ptyxv itd kcmdcmó fdh yvxdhdcmd, uthghíg itd mhgf evf qdqvf itd ytwhígc gitdeevf yáekqvf egwkvf, lkó g eg qgpg fvchdíh. 
adhv fk geotkdc df ygagn qd dcyvcmhgh dfadhgcng qvcqd cv eg xgb... fdothv itd df tc
ckñv.
Después de refrescarse el rostro y las manos, se dispuso a reponer fuerzas sacando de su mochila un pedazo de pan y algo de queso. Mientras comía pausadamente, no dejaba de mirar a un lado y a otro como si estuviera asombrado. Había conocido muchos pueblos semejantes a aquél, por eso no se explicaba la rara sensación que lo embargaba:
"Hummmm, aquí pasa algo! Algo raro tiene este pueblo!, murmuró para sus adentros.

En aquel momento, de una casa cercana a la plaza salió un niño. Con paso cansino se dirigió a la casa de al lado y llamó a la puerta. Al poco rato se le acercó otro niño y ambos se sentaron en el umbral después de un breve saludo.
Pasaba el tiempo. Los niños no hablaban entre ellos y en sus caras se reflejaban el desgano y el aburrimiento. Uno de ellos tomaba piedrecitas del suelo que luego arrojaba enfrente sin prestar atención, el otro parecía ensimismado en la contemplación de sus uñas...
El forastero los miraba sorprendido, ya que estaba acostumbrado, al llegar a un nuevo pueblo, a verse rodeado de niños que le preguntaban de dónde venía y hacia dónde iba. Aquellos dos, en cambio, parecían ignorarlo, aunque de vez en cuando lo mirasen de reojo.
El asombro del forastero fue aumentando cuando vio que otros niños iban reuniéndose alrededor de los dos primeros. Se sentaban en el suelo y permanecían allí sin decirse nada... Qué niños tan raros!
Precisamente aquella hora, la de la siesta, era la mejor para jugar libremente, lo había sido siempre, por qué no jugaban aquellos niños?, por qué teñían el aburrimiento marcado en sus miradas?
"""

    # Determine the possible valid ciphertext translations.
    letterMapping = hackSimpleSub(message)
    # Display the results to the user.
    pprint.pprint(letterMapping)
    hackedMessage = decryptWithCipherletterMapping(message, letterMapping)
    pyperclip.copy(hackedMessage)
    print(hackedMessage)
    return hackedMessage

def getBlankCipherletterMapping():
    # Returns a dictionary value that is a blank cipherletter mapping.
    return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': [],'Ü':[],'Ñ':[],'Í':[],'Ó':[],'É':[],'Á':[],'Ú':[],'Ç':[],'È':[],'Ï':[],'Û':[],'Ô':[],'Î':[],'Ë':[],'Ê':[],'Ä':[],'Â':[]}


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