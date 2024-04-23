import argparse
import datetime
import Note


def get_notes():
    try:
        with open("data.txt", "r") as file:
            notes_list = list()
            for line in file:
                if not line.isspace():
                    notes_line = line.strip().split("\t\t")
                    notes_list.append(
                        Note.Note(notes_line[0], notes_line[1], notes_line[2])
                    )
            return notes_list
    except FileNotFoundError:
        with open("data.txt", "w") as file:
            return list()


def add_note(title, message):
    notes_list = get_notes()
    with open("data.txt", "a") as f:
        for note in notes_list:
            if title == note.__getattribute__("title"):
                print("Заметка с таким заголовком уже существует")
                return
        f.write(Note.Note(title, message).__str__() + "\n\r")
        print(f"Добавлена заметка с заголовком '{title}' и сообщением '{message}'")


def list_notes():
    notes_list = get_notes()
    notes_list.sort()
    for note in notes_list:
        print(
            f"Заметка создана: {note.__getattribute__('date')}\t\tЗаголовок: {note.__getattribute__('title')}\t\tСообщение: {note.__getattribute__('message')}\t\t"
        )


def delete_note(title):
    notes_list = get_notes()
    with open("data.txt", "w") as f:
        flag = True
        for note in notes_list:
            print(note.__str__())
            if title == note.__getattribute__("title"):
                print(f"Удалена заметка с заголовком '{title}'")
                flag = False
                continue
            f.write(note.__str__() + "\n\r")
    if flag:
        print("Если вы видите это сообщение то удаление не удалось(заметка не найдена)")


def main():
    parser = argparse.ArgumentParser(description="Управление заметками")
    parser.add_argument(
        "action", choices=["add", "delete", "list"], help="Действие для выполнения"
    )
    parser.add_argument("-t", "--title", metavar="", help="Заголовок заметки")
    parser.add_argument("-m", "--msg", metavar="", help="Сообщение заметки")
    args = parser.parse_args()
    if args.action == "add":
        if not args.title or not args.msg:
            print(
                "Необходимо указать заголовок и сообщение для добавления заметки(-t title -m message)"
            )
        else:
            add_note(args.title, args.msg)
    elif args.action == "delete":
        if not args.title:
            print("Необходимо указать заголовок заметки для удаления(-t title)")
        else:
            delete_note(args.title)
    elif args.action == "list":
        list_notes()


if __name__ == "__main__":
    main()
