// DataFetchPost.test.js
import axios from 'axios';
import DataFetchPost from '../src/DataFetchFunctions/DataFetchPost'; 

// Mock do axios
jest.mock('axios');

// Mock do localStorage
const mockLocalStorage = (() => {
  let store = {};
  return {
    getItem: jest.fn((key) => store[key]),
    setItem: jest.fn((key, value) => {
      store[key] = value.toString();
    }),
    clear: jest.fn(() => {
      store = {};
    }),
  };
})();

Object.defineProperty(window, 'localStorage', { value: mockLocalStorage });

describe('DataFetchPost', () => {
  beforeEach(() => {
    // Limpa as instâncias e chamadas antes de cada teste
    jest.clearAllMocks();
    window.localStorage.clear();
  });

  it('should send a POST request with authentication and data', async () => {
    const data = { data: 'some data' };
    axios.post.mockResolvedValue({ data });
    window.localStorage.setItem('token', 'some-token');

    await expect(DataFetchPost('api/login', { user: 'user', pass: 'pass' })).resolves.toEqual({ success: "yes", data });

    expect(axios.post).toHaveBeenCalledWith('undefinedapi/login', { user: 'user', pass: 'pass' }, {
      headers: {
        Authorization: 'some-token',
      },
    });
  });

  it('should send a POST request without authentication and with data', async () => {
    const data = { data: 'some data' };
    axios.post.mockResolvedValue({ data });

    await expect(DataFetchPost('api/login', { user: 'user', pass: 'pass' })).resolves.toEqual({ success: "yes", data });

    expect(axios.post).toHaveBeenCalledWith('undefinedapi/login', { user: 'user', pass: 'pass' });
    expect(axios.post).not.toHaveBeenCalledWith(expect.objectContaining({
      headers: expect.anything(),
    }));
  });

  it('should handle a POST request failure with authentication', async () => {
    const error = 'Network Error';
    axios.post.mockRejectedValue(new Error(error));
    window.localStorage.setItem('token', 'some-token');

    await expect(DataFetchPost('api/login', { user: 'user', pass: 'pass' })).rejects.toEqual({ success: "no", error: new Error(error) });
  });

  it('should handle a POST request failure without authentication', async () => {
    const error = 'Network Error';
    axios.post.mockRejectedValue(new Error(error));

    await expect(DataFetchPost('api/login', { user: 'user', pass: 'pass' })).rejects.toEqual({ success: "no", error: new Error(error) });
  });

  it('should send a POST request with authentication but no data', async () => {
    const response = { data: 'success' };
    axios.post.mockResolvedValue(response);
    window.localStorage.setItem('token', 'some-token');

    await expect(DataFetchPost('api/submit', {})).resolves.toEqual({ success: "yes", data: response.data });

    expect(axios.post).toHaveBeenCalledWith('undefinedapi/submit', {}, {
      headers: {
        Authorization: 'some-token',
      },
    });
  });

  it('should send a POST request without authentication and no data', async () => {
    const response = { data: 'success' };
    axios.post.mockResolvedValue(response);

    await expect(DataFetchPost('api/submit', {})).resolves.toEqual({ success: "yes", data: response.data });

    expect(axios.post).toHaveBeenCalledWith('undefinedapi/submit', {});
  });

  
});
