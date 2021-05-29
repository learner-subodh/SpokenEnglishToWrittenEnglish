# defining a set of protocols for conversion
def get_protocols():
    protocols = {
                "numericals":{
                                "zero" : 0, "Zero" : 0, "one" : 1, "One" : 1, "two" : 2, "Two" : 2, "three" : 3, "Three" : 3, "four" : 4, "Four" : 4,
                                "five" : 5, "Five" : 5, "six" : 6, "Six": 6, "seven" : 7, "Seven" : 7, "eight" : 8, "Eight" : 8, "nine": 9, "Nine" : 9,
                                "ten" : 10, "Ten" : 10, "twenty" : 20, "Twenty" : 20, "thirty" : 30, "Thirty" : 30, "forty" : 40, "Forty" : 40,
                                "fifty" : 50, "Fifty" : 50, "sixty" : 60, "Sixty" : 60, "seventy" : 70, "Seventy" : 70, "eighty" : 80, "Eighty" : 80,
                                "ninety" : 90, "Ninety" : 90, "hundred" : 100, "Hundred": 100, "thousand" : 1000, "Thousand" : 1000, "lakh" : 100000,
                                "Lakh" : 100000, "million" : 1000000, "Million" : 1000000, "ten million" : 10000000, "Ten million" : 10000000, 
                                "crore" : 10000000, "Crore" : 10000000
                },
                "uples": {
                            "single" : 1, "Single" : 1, "double" : 2, "Double" : 2, "triple" : 3, "Triple" : 3, "quadruple" : 4, "Quadruple" : 4,
                            "quintuple" : 5, "Quintuple" : 5, "sextuple" : 6, "Sextuple" : 6, "septuple" : 7, "Septuple" : 7, "octuple" : 8, 
                            "Octuple" : 8, "nonuple" : 9, "Nonuple" : 9, "decuple" : 10, "Decuple" : 10
                },
                "abbr": {
                            "A M" : "AM",
                            "P M" : "PM",
                            "C M" : "CM",
                            "D M" : "DM",
                            "A S A P" : "ASAP"
                }
            }
    return protocols

#checking if a sentence has comma or full stop at front or at last or at both places, if true then return front word, sentence and last word 
def get_fw_lw(sent):
    fw, lw = "", ""
    if(len(sent)>1):
        if sent[0]==',' or sent[0]=='.':
            fw = sent[0]
            sent = sent[1:]
        if sent[-1]==',' or sent[-1]=='.':
            lw = sent[-1]
            sent = sent[:-1]
    return fw, sent, lw


# class for conversion from spoken English to written English
class SpokenEnglishToWrittenEnglish:

    def __init__(self):

        self.protocols = get_protocols()
        self.para_in = ""
        self.para_out = ""

    # function for getting input paragraph
    def get_input_para(self):

        self.para_in=input("\n[ENTER INPUT PARAGRAPH] : Please enter paragraph including spoken English:\n\t")

        if not self.para_in:
            raise ValueError("[Error]: Sorry, no input received. Please try again...")

    # function for getting output paragraph
    def show_output_para(self):
        print("\nWritten English paragraph for the given input paragraph: \n\n \"" + self.para_out + "\"")

    
    # main function for converting spoken English to written English 
    def convert(self):
        print("**************** Welcome ****************")
        # split paragraph into individual words
        words = self.para_in.split()

        # accessing defines rules
        numericals = self.protocols['numericals']
        uples = self.protocols['uples']
        abbr = self.protocols['abbr']
        i=0
        n = len(words)
        # loop trough all words in given ninput paragraph
        while i < n: 
            
            fw, w, lw = get_fw_lw(words[i])
            # Word of paragraph may of form ',dollars.', ', e mail.', ', at the rate.', etc. 
            if (i+1) != n:
            # when word is of the form e.g.: two 
                f, nextw, l = get_fw_lw(words[i+1])
                if w.lower() in numericals.keys() and (nextw.lower()=='dollars' or nextw.lower()=='dollar'):
                    self.para_out = self.para_out + " " + fw + "$" + str(numericals[w.lower()]) + lw
                    i += 2

                elif w.lower() in numericals.keys() and (nextw.lower()=='at the rate'):
                    self.para_out = self.para_out + " " + fw + "@" + str(numericals[w.lower()]) + lw
                    i += 2

                elif w.lower() in numericals.keys() and (nextw.lower()=='e mail'):
                    self.para_out = self.para_out + " " + fw + "e-mail" + str(numericals[w.lower()]) + lw
                    i += 2

                elif w.lower() in uples.keys() and len(nextw)==1:
                    # when word is of form Triple A
                    self.para_out = self.para_out + " " + f + (nextw*uples[w.lower()]) + l
                    i += 2
                elif (w+" "+nextw) in abbr.keys():
                    # if word is of form A M, P M, C M or D M
                    self.para_out = self.para_out + " " + fw + w + nextw + l
                    i += 2
                else:
                    self.para_out = self.para_out + " " + words[i]
                    i += 1
            else:
                self.para_out = self.para_out + " " + words[i]
                i += 1


#main function 
def sp_to_wr():
    # creating class object
    s2w = SpokenEnglishToWrittenEnglish()
    # accept input paragraph
    s2w.get_input_para()
    # convert spoken English to written English
    s2w.convert()
    # show converted paragraph
    s2w.show_output_para()
