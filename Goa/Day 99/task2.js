
function Car(brand, model, year) {
    this.brand = brand;
    this.model = model;
    this.year = year;
  
    this.getCarInfo = function() {
      return `${this.year} ${this.brand} ${this.model}`;
    };
  }
  
 
  const car1 = new Car("Toyota", "Camry", 2022);
  const car2 = new Car("Honda", "Civic", 2021);
  const car3 = new Car("Ford", "Mustang", 2023);
  
 
  console.log(car1.getCarInfo());
  console.log(car2.getCarInfo());
  console.log(car3.getCarInfo());
  