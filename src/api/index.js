const express = require('express');
const app = express();

// Import routes
const commandsRoute = require('./commands');

// Use routes
app.use('/api', commandsRoute);

module.exports = app;
