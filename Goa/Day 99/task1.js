
let student = {
    name: "Alice",
    age: 20,
    grade: "B",
    isEnrolled: true,
  
    getInfo: function() {
      return `Name: ${this.name}, Age: ${this.age}, Grade: ${this.grade}, Enrolled: ${this.isEnrolled}`;
    }
  };
  
  console.log(student.getInfo());
  
  
  student.grade = "A";
  

  console.log(student);
  