import { Component, OnInit } from '@angular/core';
import { GoogleService, GoogleObj } from './services/google.services';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  providers: [GoogleService]
})
export class AppComponent implements OnInit {
  public googleObj: GoogleObj = new GoogleObj();
  
  public result = '';
  private btnSubmit: any;
  private language: Object;

  constructor(private _google: GoogleService, private http:HttpClient) {
  }

  ngOnInit() {
    this.btnSubmit = document.getElementById('btnSubmit');
  }

  send() {
    this.btnSubmit.disabled = true;
    this._google.translate(this.googleObj).subscribe(
      (res: any) => {
        this.btnSubmit.disabled = false;
        this.result = res.data.translations[0].translatedText;
        console.log(res)
      },
      err => {
        console.log(err);
      }
    );
  }
}
