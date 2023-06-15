#!/usr/bin/node

const firstArg = process.env.argv[2];

if (isNaN(firstArg)) {
  console.log("Missing size");
} else {
  const n = Number(firstArg);

  const line = "";

  for (const i = 0; i < n; i++) line += "X";

  for (const i = 0; i < n; i++) console.log(line);
}
