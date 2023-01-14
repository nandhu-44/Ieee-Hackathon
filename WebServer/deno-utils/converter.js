import fs from "fs";

const file = fs.readFileSync(`${process.cwd()}/../package.json`);
const deps = JSON.parse(file).dependencies;
fs.writeFileSync(
  "../import_map.json",
  JSON.stringify({
    imports: Object.keys(deps).reduce((acc, dep) => {
      acc[dep] = `npm:${dep}@${deps[dep]}`;
      return acc;
    }, {}),
  }),
  null,
  2
);
