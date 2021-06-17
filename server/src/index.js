import Koa from "koa";
import fs from "fs";
import serve from "koa-static";
import path from "path";
import send from "koa-send";
import Router from "koa-router";

const app = new Koa();
const router = new Router();

/*
const readFiles = new Promise((resolve, reject) => {
	fs.readdir("/home/pi/Desktop/CCTV/data", (error, data) => {
		if (error) reject();		
		else resolve(data);
	});
});
*/

router.get("/list", ctx => {
/*
	readFiles.then(data => {
			ctx.body = data;
		})
		.catch(() => {
			console.log("Error: Promise is rejected");
		});
*/
	const list = fs.readdirSync("/home/pi/Desktop/CCTV/data");
	ctx.body = list;
});

/*
const getFile = filename => new Promise((resolve, reject) => {
	fs.readFile("/home/pi/Desktop/CCTV/data/" + filename, 
		(error, data) => {
			console.log("File is requested : " + filename);
			if (error) reject();
			else       resolve(data);
		});
});
*/

router.get('/file/:filename', ctx => {
	const data = fs.readFileSync("/home/pi/Desktop/CCTV/data/" + ctx.params.filename);
	ctx.body = data;
});

app.use(router.routes()).use(router.allowedMethods());

const buildDirectory = path.resolve(__dirname, "../frontend/build");
app.use(serve(buildDirectory));
app.use(async ctx =>{
	if (ctx.status === 404){
		await send(ctx, "index.html", { root : buildDirectory });
	}
});

const port = 80;
app.listen(port, () => {
	console.log("Listening to port " + port)
});
