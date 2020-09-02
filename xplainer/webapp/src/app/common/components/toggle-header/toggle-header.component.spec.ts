import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ToggleHeaderComponent } from './toggle-header.component';

describe('TogglePanelComponent', () => {
  let component: ToggleHeaderComponent;
  let fixture: ComponentFixture<ToggleHeaderComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ToggleHeaderComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ToggleHeaderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
