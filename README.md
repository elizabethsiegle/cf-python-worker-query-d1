### Query a D1 Database with Cloudflare Workers in Python

1. Create a new Cloudflare Worker from the command line with `npm create cloudflare@latest`. When prompted, give your project a name, select `Hello World example`, `Hello World Worker template`, and `Python (beta)` when asked about language.

OR

1. `git clone https://github.com/cloudflare/python-workers-examples
cd python-workers-examples/01-hello
npx wrangler@latest dev`

3. Replace the boilerplate code in a `src/main.py` with this `src/main.py` code.

4. Download this `quotes.csv` file from https://www.kaggle.com/datasets/manann/quotes-500k?select=quotes.csv

5. Save it to the `data` folder here

6. Run `python3 data/csvtosql.py`

7. Create a new D1 database in your Cloudflare dashboard <img width="1642" alt="D1 dashboard" src="https://github.com/user-attachments/assets/6c945c88-1e2e-48a7-bdb9-3295f2a19f26">


8. Import the new SQL file to D1 with `npx wrangler d1 execute {YOUR-DATABASE-NAME} --remote --file=data.sql`

9. Deploy your Worker with `npx wrangler@latest deploy`

10. Get a random quote from the database by visiting your deployed worker in the browser!<img width="1421" alt="deployed app" src="https://github.com/user-attachments/assets/131a2836-2305-4b73-a54a-50dac039108f">
