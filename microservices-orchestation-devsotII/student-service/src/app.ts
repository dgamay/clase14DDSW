import express from "express";
import "reflect-metadata";
import { sequelize } from "./config/database";
import studentController from "./controllers/studentController";

const app = express();
app.use(express.json());
app.use("/students", studentController);/* cada vez que alguien haga una solicitud a una URL que empiece con /students, usa las rutas definidas en studentController */

const PORT = 3000;

// Ruta base para probar el servidor
app.get("/", (req, res) => {
  res.send("✅ Servidor Express con TypeScript funcionando correctamente!");
});


(async () => {
  await sequelize.sync({ alter: true }); // sincroniza tablas
  app.listen(PORT, () =>
    console.log(`🚀 Server running on http://localhost:${PORT}`)
  );
})();
