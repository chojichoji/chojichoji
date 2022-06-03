from operator import length_hint
from unicodedata import name
from unittest import result


list_of_names = ['Amelia', 'Olivia', 'Emily', 'Alexey', 'Poppy', 'Ava', 'Isabella', 'Jessica', 'Marcus', 'Lily', 'Sophie', 'Grace', 'Vsevolod', 'Sophia', 'Mia', 'Evie', 'Ruby', 'Celim', 'Sumir', 'Ella', 'Scarlett', 'Ruben', 'Isabelle', 'Chloe', 'Cherlin', 'Sienna', 'Masha', 'Freya', 'Phoebe', 'Charlotte', 'Daisy', 'Alice', 'Florence', 'Eva', 'Sofia', 'Millie', 'Lucy', 'Evelyn', 'Elsie', 'Rosie', 'Imogen', 'Lola', 'Matilda', 'Elizabeth', 'Layla', 'Alasdair','Holly', 'Lilly', 'Molly', 'Erin', 'Ellie', 'Maisie', 'Maya', 'Abigail', 'Eliza', 'Georgia', 'Jasmine', 'Esme', 'Willow', 'Leanne', 'Bella', 'Annabelle', 'Keemiya', 'Ivy', 'Amber', 'Emilia', 'Emma', 'Summer', 'Hannah', 'Eleanor', 'Harriet', 'Rose', 'Amelie', 'Lexi', 'Megan', 'Gracie', 'Zara', 'Nuha', 'John', 'Lacey', 'Martha', 'Anna', 'Violet', 'Darcey', 'Maria', 'Maryam', 'Brooke', 'Aisha', 'Katie', 'Leah', 'Heinrich', 'Nour', 'Thea', 'Darcie', 'Hollie', 'Amy', 'Alexandra', 'Stephen', 'Jonathan', 'Penny', 'Mollie', 'Heidi', 'Lottie', 'Bethany', 'Francesca', 'Faith', 'Harper', 'Nancy', 'Beatrice', 'Isabel', 'Juliette', 'Darcy', 'Lydia', 'Sarah', 'Sara', 'Julia', 'Victoria', 'Zoe', 'Robyn', 'Oliver', 'Jack', 'Harry', 'Jacob', 'Charlie', 'Thomas', 'Annabel', 'George', 'Oscar', 'James', 'Ian', 'William', 'Noah', 'Alfie', 'Joshua', 'Yuvraj', 'Muhammad', 'Leo', 'Archie', 'Ethan', 'Joseph', 'Arushi', 'Freddie', 'Samuel', 'Alexander', 'Logan', 'Daniel', 'Isaac', 'Max', 'Mohammed', 'Benjamin', 'Hugo', 'Mason', 'Lucas', 'Edward', 'Harrison', 'Jake', 'Neil', 'Dylan', 'Asher', 'Riley', 'Akash', 'Finley', 'Catherine', 'Theo', 'Muktarsi', 'Sebastian', 'Adam', 'Zachary', 'Arthur', 'Thomas', 'Alberto', 'Toby', 'Jayden', 'Luke', 'Harley', 'Lewis', 'Tyler', 'Harvey', 'Anusha', 'Matthew', 'David', 'Reuben', 'Alok', 'Michael', 'Elijah', 'Kian', 'Tom', 'Mohammad', 'Blake', 'Jean', 'Luca', 'Theodore', 'Stanley', 'Derin', 'Jenson', 'Nathan', 'Nicholas', 'Charles', 'Frankie', 'Constantin', 'Jude', 'Teddy', 'Eric', 'Viren', 'Louie', 'Louis', 'Ryan', 'Hugo', 'Bobby', 'Niamh', 'Anya', 'Elliott', 'Dexter', 'Khai', 'Hariesh', 'Henry', 'Ollie', 'Aron', 'Alex', 'Liam', 'Kai', 'Gabriel', 'Connor', 'Aaron', 'Afrah', 'Frederick', 'Callum', 'Lorcan', 'Elliot', 'Albert', 'Leon', 'Ronnie', 'Rory', 'Jamie', 'Austin', 'Seth', 'Ibrahim', 'Mei', 'Owen', 'Caleb', 'Yousuf', 'Ellis', 'Sonny', 'Devyn', 'Robert', 'Joey', 'Felix', 'Finlay', 'Rossa', 'Ekraj', 'Jackson', 'Jimi', 'Meera', 'Rafi', 'Salahdeen', 'Guido', 'Tanya', 'Karlis']
list_of_names_1=list_of_names[:30]

"""
def find_names_starting_with(letter):
    result=[] 
    for name in list_of_names:
        if name[0]==letter:
            result.append(name)
    return result
user_input=input("Enter a Letter to Search: ")

print(find_names_starting_with(user_input))
def find__length_of_names(length):
    result=[]
    count=0
    for name in list_of_names:
        if len(name)==length:
            result.append(name)
        count+=1
    return result
length_of_name=int(input("Enter a number: "))
print(find__length_of_names(length_of_name))
"""
#This function can go through any list and sort if by first letter & length of letters in a name on the list
def find_names_starting_with(letter, names):
    result=[]
    for name in names:
        if name[0]==letter:
            result.append(name)
    return result

def find_length_of_names(length, names):
    result=[]
    for name in names:
        if len(name)==length:
            result.append(name)
    return result
#user_input=input("Enter a letter to search: ")
#print(find_names_starting_with(user_input, list_of_names))


names_starting_with_e=find_names_starting_with("E", list_of_names)
print(names_starting_with_e)
length_of_name=int(input("Enter a number: "))
print(find_length_of_names(length_of_name, names_starting_with_e))
#print(find_names_starting_with(user_input, list_of_names_1))
#length_of_name=int(input("Enter a number: "))
#print(find_length_of_names(length_of_name, user_input))