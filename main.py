import json
import datetime


def save_notes(notes, filename):
    with open(filename, 'w') as file:
        json.dump(notes, file)


def load_notes(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def add_note(notes):
    note_id = input("Enter note ID: ")
    title = input("Enter note title: ")
    body = input("Enter note body: ")
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes[note_id] = {'title': title, 'body': body, 'date_time': date_time}
    print("Note added successfully!")


def edit_note(notes):
    note_id = input("Enter note ID to edit: ")
    if note_id in notes:
        title = input("Enter new title: ")
        body = input("Enter new body: ")
        notes[note_id]['title'] = title
        notes[note_id]['body'] = body
        notes[note_id]['date_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Note edited successfully!")
    else:
        print("Note not found!")


def delete_note(notes):
    note_id = input("Enter note ID to delete: ")
    if note_id in notes:
        del notes[note_id]
        print("Note deleted successfully!")
    else:
        print("Note not found!")


def print_notes(notes):
    for note_id, note_info in notes.items():
        print(f"Note ID: {note_id}")
        print(f"Title: {note_info['title']}")
        print(f"Body: {note_info['body']}")
        print(f"Date/Time: {note_info['date_time']}")
        print("-" * 30)


def main():
    filename = 'notes.json'
    notes = load_notes(filename)

    while True:
        print("\nOptions:")
        print("1. Add Note")
        print("2. Edit Note")
        print("3. Delete Note")
        print("4. Print Notes")
        print("5. Save and Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_note(notes)
        elif choice == '2':
            edit_note(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            print_notes(notes)
        elif choice == '5':
            save_notes(notes, filename)
            print("Notes saved. Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
