import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ModelOverviewComponent } from './model-overview.component';

describe('ModelOverviewComponent', () => {
  let component: ModelOverviewComponent;
  let fixture: ComponentFixture<ModelOverviewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ModelOverviewComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ModelOverviewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
