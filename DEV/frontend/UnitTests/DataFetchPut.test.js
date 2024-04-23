// DataFetchPut.test.js
import axios from 'axios';
import DataFetchPut from '../src/DataFetchFunctions/DataFetchPut'; 

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

describe('DataFetchPut', () => {
  beforeEach(() => {
    // Limpa as instâncias e chamadas antes de cada teste
    jest.clearAllMocks();
    window.localStorage.clear();
  });

  it('should send a PUT request with authentication and data', async () => {
    const data = { data: 'some data' };
    axios.put.mockResolvedValue({ data });
    window.localStorage.setItem('token', 'some-token');

    await expect(DataFetchPut('api/update', { newData: 'new data' })).resolves.toEqual({ success: "yes", data });

    expect(axios.put).toHaveBeenCalledWith('undefinedapi/update', { newData: 'new data' }, {
      headers: {
        Authorization: 'some-token',
      },
    });
  });

  it('should send a PUT request without authentication and with data', async () => {
    const data = { data: 'some data' };
    axios.put.mockResolvedValue({ data });

    await expect(DataFetchPut('api/update', { newData: 'new data' })).resolves.toEqual({ success: "yes", data });

    expect(axios.put).toHaveBeenCalledWith('undefinedapi/update', { newData: 'new data' });
    expect(axios.put).not.toHaveBeenCalledWith(expect.objectContaining({
      headers: expect.anything(),
    }));
  });

  it('should handle a PUT request failure with authentication', async () => {
    const error = 'Network Error';
    axios.put.mockRejectedValue(new Error(error));
    window.localStorage.setItem('token', 'some-token');

    await expect(DataFetchPut('api/update', { newData: 'new data' })).rejects.toEqual({ success: "no", error: new Error(error) });
  });

  it('should handle a PUT request failure without authentication', async () => {
    const error = 'Network Error';
    axios.put.mockRejectedValue(new Error(error));

    await expect(DataFetchPut('api/update', { newData: 'new data' })).rejects.toEqual({ success: "no", error: new Error(error) });
  });

  it('should send a PUT request with authentication but no data', async () => {
    const response = { data: 'update success' };
    axios.put.mockResolvedValue(response);
    window.localStorage.setItem('token', 'some-token');

    await expect(DataFetchPut('api/update', {})).resolves.toEqual({ success: "yes", data: response.data });

    expect(axios.put).toHaveBeenCalledWith('undefinedapi/update', {}, {
      headers: {
        Authorization: 'some-token',
      },
    });
  });

  it('should send a PUT request without authentication and no data', async () => {
    const response = { data: 'update success' };
    axios.put.mockResolvedValue(response);

    await expect(DataFetchPut('api/update', {})).resolves.toEqual({ success: "yes", data: response.data });

    expect(axios.put).toHaveBeenCalledWith('undefinedapi/update', {});
  });

  
});
