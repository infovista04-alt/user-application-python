const request = require('supertest');
const app = require('../src/index');

describe('Health Endpoints', () => {
  test('GET / returns healthy status', async () => {
    const res = await request(app).get('/');
    expect(res.status).toBe(200);
    expect(res.body.status).toBe('healthy');
  });

  test('GET /health returns detailed health', async () => {
    const res = await request(app).get('/health');
    expect(res.status).toBe(200);
    expect(res.body).toHaveProperty('uptime');
  });
});

describe('Items Endpoints', () => {
  test('GET /api/items returns array', async () => {
    const res = await request(app).get('/api/items');
    expect(res.status).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  });

  test('POST /api/items creates item', async () => {
    const res = await request(app)
      .post('/api/items')
      .send({ name: 'Test', price: 9.99 });
    expect(res.status).toBe(201);
    expect(res.body.name).toBe('Test');
  });

  test('POST /api/items validates input', async () => {
    const res = await request(app)
      .post('/api/items')
      .send({});
    expect(res.status).toBe(400);
  });
});
