// Alex Miller
// Axios creation and API requests

import axios from 'axios';
import type { Item } from '../types/Item';

// create the API
const api = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/', // url of Django server
    withCredentials: false, // no credentials needed
});


/* Functions to call to make API Requests: */

// get all items
export const getItems = () => api.get<Item[]>('items/');

// create a new item
export const createItem = (data: Omit<Item, 'id'>) => api.post<Item>('items/', data);

// update an item
export const updateItem = (id: number, data: Partial<Item>) => api.put<Item>(`items/${id}/`, data);

// delete an item
export const deleteItem = (id: number) => api.delete(`items/${id}/`);

