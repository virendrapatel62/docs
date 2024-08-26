import express from "express";

const app = express();

const PORT = 3000;

app.listen(3000, () => {
  console.log(`Listening on Port ${PORT}`);
});

app.get("/", (request, response) => {
  response.json({
    message: "Api is working..",
  });
});

app.get("/api/ping", (_, response) => {
  response.json("Pong");
});
