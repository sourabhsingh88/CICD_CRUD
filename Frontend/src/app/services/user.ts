import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { User } from '../models/user.model';
import { API_BASE_URL } from '../api.config';

@Injectable({ providedIn: 'root' })
export class UserService {
  private http = inject(HttpClient);
  private baseUrl = inject(API_BASE_URL);

  private API = `${this.baseUrl}/user`;

  getAll() {
    return this.http.get<User[]>(`${this.API}/all`);
  }

  create(user: User) {
    return this.http.post(`${this.API}/create`, user);
  }

  update(email: string, user: User) {
    return this.http.put(`${this.API}/email/${email}`, user);
  }

  delete(email: string) {
    return this.http.delete(`${this.API}/email/${email}`);
  }
}
