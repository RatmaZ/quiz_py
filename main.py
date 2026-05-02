from flask import Flask
import db_scripts as db
from db_scripts import get_question_after
from random import randint
db.create()
db.open()

counter = 0

def index():
   quizes = db.show('quiz')
   html = '''
      <html>
      <head>
         <title>Выбор викторины</title>
         <style>
               body { font-family: Arial; margin: 50px; text-align: center; }
               .quiz-btn { 
                  display: block; 
                  margin: 10px auto; 
                  padding: 15px 30px; 
                  font-size: 18px;
                  background-color: #4CAF50;
                  color: white;
                  border: none;
                  cursor: pointer;
                  text-decoration: none;
                  width: 300px;
               }
               .quiz-btn:hover { background-color: #45a049; }
               h1 { color: #333; }
         </style>
      </head>
      <body>
         <h1>Выберите викторину:</h1>
      '''
      
   for quiz_item in quizes:
      quiz_id = quiz_item[0]
      quiz_name = quiz_item[1]
      html += f'<a href="/test?quiz_id={quiz_id}" class="quiz-btn">{quiz_name}</a><br>'
      
      html += '''
      </body>
      </html>
      '''
   return html

def parse_question(question):
    return {
        'text': question[1],
        'answer': question[2],
        'wrong1': question[3],
        'wrong2': question[4],
        'wrong3': question[5]
    }
def test():
    num = randint(0, 5)
    question_data = get_question_after(num, 1)
    if question_data is None:
        return "Вопросов больше нет"
    question = parse_question(question_data)
    return f'''
    <html>
        <body>
            <h3>{question['text']}</h3>
            <p>{question['answer']}</p>
            <p>{question['wrong1']}</p>
            <p>{question['wrong2']}</p>
            <p>{question['wrong3']}</p>
        </body>
    </html>
    '''

def result():
      
   return f'''
   <title>Результат викторины</title>
   <h1>Результат:</h1>
   <h3>{counter} правильных из 6<h3>
   
   '''



app = Flask(__name__) 

app.add_url_rule('/', 'index', index)  
app.add_url_rule('/test', 'test', test)
app.add_url_rule('/result', 'result', result)
if __name__ == "__main__":
    # Запускаем веб-сервер:
    app.run(host=('0.0.0.0'))