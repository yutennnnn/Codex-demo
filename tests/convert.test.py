const { execSync } = require('child_process');
const fs = require('fs');
const assert = require('assert');

if (fs.existsSync('tasks.md')) fs.unlinkSync('tasks.md');
execSync('pnpm run generate', { stdio: 'inherit' });
assert.ok(fs.existsSync('tasks.md'), 'tasks.md not generated');
const content = fs.readFileSync('tasks.md', 'utf8');
assert.ok(content.includes('Buy bitcoin'), 'Buy bitcoin missing');
console.log('All tests passed.');

