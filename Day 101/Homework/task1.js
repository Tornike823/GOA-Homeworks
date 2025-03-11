


const university = {
  name: "თბილისის სახელმწიფო უნივერსიტეტი",
  departments: 15,
  website: "www.tsu.ge",
  ratings: {
    student1: 4.5,
    student2: 4.0,
    student3: 3.8,
  },
};


console.log(university);


console.log(university.hasOwnProperty("scholarship")); 


university.studentsCount = 10000;


Object.freeze(university);


university.name = "ახალი სახელი"; 


console.log(Object.isFrozen(university));