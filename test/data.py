from random import shuffle

# class Test:
#     def init(self, quest_list, quantity = 5):

#         # self.current_quest = 0

class Questions:
    def __init__(self, question, right, wrong1, wrong2, wrong3, img = None):
        self.question = question
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        self.img = img
    
    def show_data(self, quest_lb, result_answ, rbtn_list):
        quest_lb.setText(self.question + "<br>" + f"<img src={self.img} height=100>")
        result_answ.setText(self.right)
        shuffle(rbtn_list)
        rbtn_list[0].setText(self.right)
        rbtn_list[1].setText(self.wrong1)
        rbtn_list[2].setText(self.wrong2)
        rbtn_list[3].setText(self.wrong3)

    def show_data_study(self, pict_lb, answ_lb):
        pict_lb.setText(f"<img src={self.img} height=100>")
        answ_lb.setText(self.right)

    def chek_result(self, rbtn_list, result):
        if rbtn_list[0].isChecked():
            result.setText("вірно!")
        else:
            result.setText("не вірно!")

q1 = Questions("У якому році ввели у стрій лінкор King Georg 5", "1940", "1939", "1941", "1945", "princeofwales.jpg")
q2 = Questions("У якому році ввели у стрій лінкор Bismark", "1940", "1933", "1914", "1942", "bismark.jpg")
q3 = Questions("У якому році ввели у стрій лінкор Nevada", "1916", "1937", "1932", "1922", "nevada.jpg")
q4 = Questions("У якому році ввели у стрій лінкор Yamato", "1941", "1911", "1943", "1929", "yamato.jpg")
q5 = Questions("У якому році ввели у стрій крейсер Alaska", "1944", "2017", "1923", "1947", "alaska.jpg")
q6 = Questions("У якому році ввели у стрій крейсер Prinz Eugen", "1939", "1940", "1934", '1932', "Eugen.png")
q7 = Questions("У якому році ввели у стрій лінкор Elizabeth", "1915", "1920", "1930", "1900", "elizabeth.jpg")
q8 = Questions("У якому році ввели у стрій лінкор Dreadnought", "1906", "1903", "1917", "1879", "dreadnought.jpg")
q9 = Questions("У якому році ввели у стрій лінкор Jersey", "1942", "1905", "1940", "1953", "jersey.jpg")


quest_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9]