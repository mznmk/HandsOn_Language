const person = {
  name: 'yota',
  age: 30,
  hobbies: ['Sports', 'Cooking']
};

let favoriteActivities: string[];
favoriteActivities = ['Sports'];

console.log(person.name);

for (const hobby of person.hobbies) {
  // console.log(hobby);
  console.log(hobby.toUpperCase());
}