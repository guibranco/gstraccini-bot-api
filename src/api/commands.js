const express = require('express');
const router = express.Router();

// Mock command registry
const commandRegistry = [
  {
    name: 'listUsers',
    description: 'Lists all users in the system.',
    parameters: ['page', 'limit'],
    examples: ['GET /users?page=1&limit=10']
  },
  {
    name: 'createUser',
    description: 'Creates a new user.',
    parameters: ['name', 'email'],
    examples: ['POST /users { "name": "John", "email": "john@example.com" }']
  }
];

// Helper functions to format command data
function formatAsMarkdown(commands) {
  return commands.map(cmd => `## ${cmd.name}\n\n${cmd.description}\n\n**Parameters**: ${cmd.parameters.join(', ')}\n\n**Examples**: ${cmd.examples.join(', ')}\n`).join('\n');
}

function formatAsHTML(commands) {
  return commands.map(cmd => `<h2>${cmd.name}</h2><p>${cmd.description}</p><strong>Parameters</strong>: ${cmd.parameters.join(', ')}<br><strong>Examples</strong>: ${cmd.examples.join(', ')}<br>`).join('');
}

// /commands endpoint
router.get('/commands', (req, res) => {
  const format = req.query.format || 'markdown';
  let response;

  if (format === 'markdown') {
    res.setHeader('Content-Type', 'text/markdown');
    response = formatAsMarkdown(commandRegistry);
  } else if (format === 'html') {
    res.setHeader('Content-Type', 'text/html');
    response = formatAsHTML(commandRegistry);
  } else {
    return res.status(400).json({ error: 'Unsupported format. Use "markdown" or "html".' });
  }

  res.send(response);
});

module.exports = router;
