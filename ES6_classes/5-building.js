export default class Building {
  constructor(sqft){
	if (new.target === Building){
      throw new Error('You cannot instantiate an abstract class directly')
	}
	this.sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(value) {
    if (typeof value !== 'number'){
      throw new TypeError('Sqft must be a number')
	}
	this._sqft = value;
  }

  evacuationWarningMessage(){
	throw new Error('the method evacuationWarningMessage must be implemented')
  }
}
