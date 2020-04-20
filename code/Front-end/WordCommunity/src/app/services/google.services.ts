import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class GoogleService {
  constructor(private _http: HttpClient) {}
  key:String = "AIzaSyAt2tTns-wNG2lP2nGkBqoNtPQ5AFsDYqA"
  translate(obj: GoogleObj) {
    return this._http.post(url + this.key, obj);
  }
}

const url = 'https://translation.googleapis.com/language/translate/v2?key=';

export class GoogleObj {
   q: string;
   source: string = 'en';
   target: string = 'it';
   format: string = 'text';

  constructor() {}
}
