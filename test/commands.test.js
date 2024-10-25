const request = require('supertest');
const app = require('../src/api');

describe('GET /api/commands', () => {
  it('should return commands in markdown format by default', async () => {
    const res = await request(app)
      .get('/api/commands')
      .expect('Content-Type', /text\/markdown/)
      .expect(200);
    expect(res.text).toContain('## listUsers');
    expect(res.text).toContain('Lists all users in the system.');
  });

  it('should return commands in html format when specified', async () => {
    const res = await request(app)
      .get('/api/commands?format=html')
      .expect('Content-Type', /text\/html/)
      .expect(200);
    expect(res.text).toContain('<h2>listUsers</h2>');
    expect(res.text).toContain('<p>Lists all users in the system.</p>');
  });

  it('should return 400 for unsupported format', async () => {
    const res = await request(app)
      .get('/api/commands?format=xml')
      .expect('Content-Type', /json/)
      .expect(400);
    expect(res.body.error).toBe('Unsupported format. Use "markdown" or "html".');
  });
});
