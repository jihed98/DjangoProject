import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TranslateTextComponent } from './translate-text.component';

describe('TranslateTextComponent', () => {
  let component: TranslateTextComponent;
  let fixture: ComponentFixture<TranslateTextComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TranslateTextComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TranslateTextComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
