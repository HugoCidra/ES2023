// DataFetchGet.test.js
import axios from 'axios';
import DataFetchGet from '../src/DataFetchFunctions/DataFetchGet'; 
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

describe('DataFetchGet', () => {
  beforeEach(() => {
    // Limpa as instâncias e chama contagens antes de cada teste
    jest.clearAllMocks();
    window.localStorage.clear();
  });

  it('should fetch data successfully with token', async () => {
    const data = { data: 'some data' };
    axios.get.mockResolvedValue({ data }); // Mock da resposta de axios.get
    window.localStorage.setItem('token', 'some-token'); // Configura um token mock

    await expect(DataFetchGet('api/some-endpoint')).resolves.toEqual({ success: "yes", data });

    expect(axios.get).toHaveBeenCalledWith('undefinedapi/some-endpoint', {
      headers: {
        Authorization: 'some-token',
      },
    });
  });

  it('should fetch data with token and query params', async () => {
    const data = { data: 'some data' };
    const queryParams = { key: 'value' };
    axios.get.mockResolvedValue({ data });
    window.localStorage.setItem('token', 'some-token');

    await expect(DataFetchGet('api/some-endpoint', queryParams)).resolves.toEqual({ success: "yes", data });

    expect(axios.get).toHaveBeenCalledWith('undefinedapi/some-endpoint', {
      headers: {
        Authorization: 'some-token',
      },
      params: queryParams,
    });
  });

  it('should fetch data without token', async () => {
    const data = { data: 'some data' };
    axios.get.mockResolvedValue({ data });

    await expect(DataFetchGet('api/some-endpoint')).resolves.toEqual({ success: "yes", data });

    expect(axios.get).toHaveBeenCalledWith('undefinedapi/some-endpoint');
  });

  it('should handle request failure', async () => {
    const error = 'Network Error';
    axios.get.mockRejectedValue(new Error(error));

    await expect(DataFetchGet('api/some-endpoint')).rejects.toEqual({ success: "no", error: new Error(error) });
  });
});

it('should make an unauthenticated request if token is not present', async () => {
  const data = { data: 'public data' };
  axios.get.mockResolvedValue({ data });

  // Não definir um token aqui simula a ausência de um token no localStorage
  await expect(DataFetchGet('api/public-endpoint')).resolves.toEqual({ success: "yes", data });

  expect(axios.get).toHaveBeenCalledWith('undefinedapi/public-endpoint');
  expect(axios.get).not.toHaveBeenCalledWith(expect.objectContaining({
    headers: expect.anything(),
  }));
});

it('should fetch data without token and with query params', async () => {
  const data = { data: 'some data' };
  const queryParams = { key: 'value' };
  axios.get.mockResolvedValue({ data });

  // Novamente, não definir um token aqui simula a ausência de um token no localStorage
  await expect(DataFetchGet('api/public-endpoint', queryParams)).resolves.toEqual({ success: "yes", data });

  expect(axios.get).toHaveBeenCalledWith('undefinedapi/public-endpoint', {
    params: queryParams,
  });
});

