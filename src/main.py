import models.person
import repository.person_repository

def main():
    #new_person = models.person.person('camila', 'camiscd.santos@outlook.com', 20000, 40)
    #repository.person_repository.create_new_person(new_person)
    # repository.person_repository.delete_person(1)
    persons = repository.person_repository.get_all_persons()

    for p in persons:
        print(p)

if __name__ == "__main__":
    main()