import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { UserService } from '../services/user';
import { User } from '../models/user.model';

@Component({
  selector: 'app-user',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './user.html',
  styleUrls: ['./user.css']
})
export class UserComponent {

  users: User[] = [];

  // form state
  name = '';
  email = '';

  // edit state
  isEdit = false;
  editEmail: string | null = null;

  constructor(private service: UserService) {
    this.loadUsers();
  }

  loadUsers() {
    this.service.getAll().subscribe(res => this.users = res);
  }

  submit() {
    const payload: User = {
      name: this.name,
      email: this.email
    };

    if (this.isEdit && this.editEmail) {
      // UPDATE
      this.service.update(this.editEmail, payload).subscribe(() => {
        this.resetForm();
        this.loadUsers();
      });
    } else {
      // CREATE
      this.service.create(payload).subscribe(() => {
        this.resetForm();
        this.loadUsers();
      });
    }
  }

  edit(user: User) {
    this.isEdit = true;
    this.editEmail = user.email;
    this.name = user.name;
    this.email = user.email;
  }

  delete(email: string) {
    this.service.delete(email).subscribe(() => {
      this.loadUsers();
    });
  }

  resetForm() {
    this.name = '';
    this.email = '';
    this.isEdit = false;
    this.editEmail = null;
  }
}
