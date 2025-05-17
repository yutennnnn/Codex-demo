const fs = require('fs');

function generate() {
  const data = fs.readFileSync('tasks.json', 'utf8');
  const tasks = JSON.parse(data);
  let md = '| id | title |\n| --- | ----- |\n';
  for (const task of tasks) {
    md += `| ${task.id} | ${task.title} |\n`;
  }
  fs.writeFileSync('tasks.md', md);
}

if (require.main === module) {
  generate();
}

module.exports = generate;
