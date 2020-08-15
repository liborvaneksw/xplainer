import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ModelPlotComponent } from './model-plot.component';

describe('ModelPlotComponent', () => {
  let component: ModelPlotComponent;
  let fixture: ComponentFixture<ModelPlotComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ModelPlotComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ModelPlotComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
