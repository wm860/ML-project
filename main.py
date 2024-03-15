from bayes_forest import *
import PySimpleGUI as sg

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def classification():
    filename = "car.data"
    data = read_data(filename)
    train_data, test_data = split_data(data)    # Split the data into training and testing sets
    x_train, y_train = encoding(train_data)
    x_test, y_test = encoding(test_data)
    random_forest = RandomForest(100, NaiveBayes)  # Create a random forest with 100 trees of naive bayes classifications
    random_forest.fit(x_train, y_train)
    y_pred = random_forest.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy}")
def classification2():
    filename_obesity = "ObesityDataSet.csv"
    filename_app_data = "data_to_classification.csv"
    data_obesity = read_data(filename_obesity, 16)
    data_to_classification = read_data(filename_app_data,16)
    train_data_obesity, test_data_obesity = split_data(data_obesity)
    x_train_obesity, y_train_obesity = encoding(train_data_obesity)
    x_test_obesity, y_test_obesity = encoding(test_data_obesity)

    x_to_predict, y_to_predict = encoding(data_to_classification)

    random_forest = RandomForest(30,NaiveBayes)  # Create a random forest with 100 trees of naive bayes classifications
    random_forest.fit(x_train_obesity, y_train_obesity)
    y_pred2 = random_forest.predict(x_test_obesity)
    y_predicted = random_forest.predict(x_to_predict)
    accuracy = accuracy_score(y_test_obesity, y_pred2)
    print(f"Accuracy2: {accuracy}")
def classification3():
    filename_cancer = "breast-cancer.data"
    filename_app_data = "breast_data_to_classification.data"
    data_cancer = read_data(filename_cancer, 0)
    data_to_classification = read_data(filename_app_data,0)
    train_data_cancer, test_data_cancer = split_data(data_cancer)
    x_train_cancer, y_train_cancer = encoding(train_data_cancer)
    x_test_cancer, y_test_cancer = encoding(test_data_cancer)

    x_to_predict, y_to_predict = encoding(data_to_classification)

    random_forest = RandomForest(30,NaiveBayes)  # Create a random forest with 100 trees of naive bayes classifications
    random_forest.fit(x_train_cancer, y_train_cancer)
    y_pred2 = random_forest.predict(x_test_cancer)
    y_predicted = random_forest.predict(x_to_predict)
    accuracy = accuracy_score(y_test_cancer, y_pred2)
    print(f"Accuracy3: {accuracy}")
    print(y_predicted)
def classification4():
    filename_cancer = "breast-cancer.data"
    filename_app_data = "breast_data_to_classification_poll.csv"
    data_cancer = read_data(filename_cancer, 0)
    data_to_classification = read_data(filename_app_data,0)
    train_data_cancer, test_data_cancer = split_data(data_cancer)
    x_train_cancer, y_train_cancer = encoding(train_data_cancer)
    x_test_cancer, y_test_cancer = encoding(test_data_cancer)

    x_to_predict, y_to_predict = encoding(data_to_classification)

    random_forest = RandomForest(30,NaiveBayes)  # Create a random forest with 100 trees of naive bayes classifications
    random_forest.fit(x_train_cancer, y_train_cancer)
    y_pred2 = random_forest.predict(x_test_cancer)
    y_predicted = random_forest.predict(x_to_predict)
    accuracy = accuracy_score(y_test_cancer, y_pred2)
    print(f"Accuracy3: {accuracy}")
    print(y_predicted)
    return accuracy, y_predicted

def gui2():
    layout = [
        [sg.Text('Breast cancer predisposition poll', size=(30, 1), font=("Helvetica", 25), text_color='green')],
        [sg.Text('1. Pytanie : Podaj wiek')],
        [sg.Radio('Opcja 1', "RADIO1", key='-RADIO1-', default=True)],
        #[sg.Checkbox('Mój checkbox'), sg.Checkbox('Mój kolejny checkbox!', default=True)],
        [sg.Radio('Radio button! ', "RADIO1", default=True), sg.Radio('Inny button !', "RADIO1")],
        [sg.Text('2. Pytanie : Podaj ilość dzieci')],
        [sg.Radio('Radio button! ', "RADIO2", default=True), sg.Radio('Inny button !', "RADIO2")],
        [sg.Multiline(default_text='To jest domyślny tekst, jeśli zdecydujesz się nie wpisywać niczego',
                      size=(70, 10))],
        [sg.Button('OK'), sg.Button('Anuluj')],
        [sg.InputCombo(['Combobox 1', 'Combobox 2'], size=(20, 3)),
         sg.Slider(range=(1, 100), orientation='h', size=(35, 20), default_value=85)],
        [sg.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'], size=(30, 6)),
         sg.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=25),
         sg.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=75),
         sg.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=10)],
        [sg.Text('_' * 100, size=(70, 1))],
        [sg.Text('Wybierz katalogi: źródłowy i docelowy', size=(35, 1))],
        [sg.Text('Wybierz katalog', size=(15, 1), auto_size_text=False, justification='right'), sg.InputText('Źródło'),
         sg.FolderBrowse()],
        [sg.Text('Docelowy katalog', size=(15, 1), auto_size_text=False, justification='right'),
         sg.InputText('Docelowo'), sg.FolderBrowse()],
        [sg.Submit(), sg.Cancel(), sg.SimpleButton('Dostosowany', button_color=('white', 'green'))]
    ]

    window = sg.Window(title='Wszystko razem - ABIX', layout=layout, auto_size_text=True, default_element_size=(40, 1))
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'OK':
            break
    #button, values = window.read()
def gui3():
    layout = \
    [
        [sg.Text('Select your age:')],
        [sg.Combo(['10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79'], key='-OPTION-', default_value='10-19')],
        [sg.Text('Menopause status:')],
        [sg.Combo(['lt40', 'ge40', 'premeno'], key='-OPTION2-', default_value='premeno')],
        [sg.Text('Tumor size:')],
        [sg.Combo(['0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59'], key='-OPTION3-', default_value='0-4')],
        [sg.Text('INV nodes:')],
        [sg.Combo(
            ['0-2', '3-5', '6-8', '9-11', '12-14', '15-17', '18-20', '21-23', '24-26', '27-29', '30-32', '33-35', '36-39'],
            key='-OPTION4-', default_value='0-2')],
        [sg.Text('Node caps:')],
        [sg.Combo(['yes', 'no'], key='-OPTION5-', default_value='no')],
        [sg.Text('Deg malig:')],
        [sg.Combo(['1', '2', '3'], key='-OPTION6-', default_value='1')],
        [sg.Text('Breast:')],
        [sg.Combo(['left', 'right'], key='-OPTION7-', default_value='left')],
        [sg.Text('Breast quad:')],
        [sg.Combo(['left-up', 'left-low', 'right-up','right-low', 'central'], key='-OPTION8-', default_value='left-up')],
        [sg.Text('irradiat:')],
        [sg.Combo(['yes', 'no'], key='-OPTION8-', default_value='yes')],
        [sg.Button('OK'), sg.Button('Anuluj')]
    ]
    window = sg.Window('cancer app', layout)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Anuluj':
            break
        elif event == 'OK':
            selected_option1 = values['-OPTION-']
            selected_option2 = values['-OPTION2-']
            selected_option3 = values['-OPTION3-']
            selected_option4 = values['-OPTION4-']
            selected_option5 = values['-OPTION5-']
            selected_option6 = values['-OPTION6-']
            selected_option7 = values['-OPTION7-']
            selected_option8 = values['-OPTION8-']
            options = [selected_option1, selected_option2, selected_option3, selected_option4, selected_option5, selected_option6, selected_option7, selected_option8]
            sg.popup(f'Your responses: {selected_option1}, {selected_option2}, {selected_option3}, {selected_option4}, {selected_option5}, {selected_option6}, {selected_option7}, {selected_option8}')
            return options
    window.close()
    #return options
def gui_final(acc, pred):
    layout = \
    [
        [sg.Text('Your predisposition to breast cancer is:')],
        [sg.Text(f'{pred} with AI accuracy of: {acc}')]
    ]
    window = sg.Window('cancer app', layout)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
    window.close()
def save_data_to_file(data):
    data = [item.replace("[", "").replace("]", "").replace("'", "") for item in data]
    data_string = ','.join(data)
    with open('breast_data_to_classification_poll.csv', 'w') as file:
        file.write(data_string + '\n')

if __name__ == '__main__':

    a=gui3()
    a.insert(0, 'no_class')
    print(a)
    save_data_to_file(a)
    acc, pred = classification4()
    gui_final(acc,pred)
    displayText()

