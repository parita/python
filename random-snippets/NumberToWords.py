class Number2Words(object):

    def __init__(self):
        '''Initialise the class with useful data'''

        self.wordsDict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
                          8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
                          14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
                          18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
                          50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninty' }

        self.powerNameList = ['thousand', 'lac', 'crore']


    def convertNumberToWords(self, number):

        # Check if there is decimal in the number. If Yes process them as paisa part.
        formString = str(number)
        if formString.find('.') != -1:
            withoutDecimal, decimalPart = formString.split('.')

            paisaPart =  str(round(float(formString), 2)).split('.')[1]
            inPaisa = self._formulateDoubleDigitWords(paisaPart)

            formString, formNumber = str(withoutDecimal), int(withoutDecimal)
        else:
            # Process the number part without decimal separately
            formNumber = int(number)
            inPaisa = None

        if not formNumber:
            return 'zero'

        self._validateNumber(formString, formNumber)

        inRupees = self._convertNumberToWords(formString)

        if inPaisa:
            return 'Rs. %s and %s paisa' % (inRupees.title(), inPaisa.title())
        else:
            return 'Rs. %s' % inRupees.title()


    def _validateNumber(self, formString, formNumber):

        assert formString.isdigit()

        # Developed to provide words upto 999999999
        if formNumber > 999999999 or formNumber < 0:
            raise AssertionError('Out Of range')


    def _convertNumberToWords(self, formString):

        MSBs, hundredthPlace, teens = self._getGroupOfNumbers(formString)

        wordsList = self._convertGroupsToWords(MSBs, hundredthPlace, teens)

        return ' '.join(wordsList)


    def _getGroupOfNumbers(self, formString):

        hundredthPlace, teens = formString[-3:-2], formString[-2:]

        msbUnformattedList = list(formString[:-3])

        #---------------------------------------------------------------------#

        MSBs = []
        tempstr = ''
        for num in msbUnformattedList[::-1]:
            tempstr = '%s%s' % (num, tempstr)
            if len(tempstr) == 2:
                MSBs.insert(0, tempstr)
                tempstr = ''
        if tempstr:
            MSBs.insert(0, tempstr)

        #---------------------------------------------------------------------#

        return MSBs, hundredthPlace, teens


    def _convertGroupsToWords(self, MSBs, hundredthPlace, teens):

        wordList = []

        #---------------------------------------------------------------------#
        if teens:
            teens = int(teens)
            tensUnitsInWords = self._formulateDoubleDigitWords(teens)
            if tensUnitsInWords:
                wordList.insert(0, tensUnitsInWords)

        #---------------------------------------------------------------------#
        if hundredthPlace:
            hundredthPlace = int(hundredthPlace)
            if not hundredthPlace:
                # Might be zero. Ignore.
                pass
            else:
                hundredsInWords = '%s hundred' % self.wordsDict[hundredthPlace]
                wordList.insert(0, hundredsInWords)

        #---------------------------------------------------------------------#
        if MSBs:
            MSBs.reverse()

            for idx, item in enumerate(MSBs):
                inWords = self._formulateDoubleDigitWords(item)
                if inWords:
                    inWordsWithDenomination = '%s %s' % (inWords, self.powerNameList[idx])
                    wordList.insert(0, inWordsWithDenomination)

        #---------------------------------------------------------------------#
        return wordList


    def _formulateDoubleDigitWords(self, doubleDigit):

        if not int(doubleDigit):
            # Might be zero. Ignore.
            return None
        elif self.wordsDict.has_key(int(doubleDigit)):
            # Global dict has the key for this number
            tensInWords = self.wordsDict[int(doubleDigit)]
            return tensInWords
        else:
            doubleDigitStr = str(doubleDigit)
            tens, units = int(doubleDigitStr[0])*10, int(doubleDigitStr[1])
            tensUnitsInWords = '%s %s' % (self.wordsDict[tens], self.wordsDict[units])
            return tensUnitsInWords


# if __name__ == '__main__':

#     wGenerator = Number2Words()
#     print wGenerator.convertNumberToWords(437345)