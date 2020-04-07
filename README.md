# Trans19

An individual project for HKU COMP3297 Software Engineering course. It's main objective is to allow 
pandemic patient management and visualization, as well as epidemiology analysis.

The backend consists of a Django
application that uses GraphQL as API, which can be navigated in http://127.0.0.1:8000/playground/.

The frontend consists of a React application that uses Next.js, Material-UI and Apollo Client. You 
can run its development instance by running `yarn start` in the `browser` directory.

There are also `docker-compose` integration on plan, which wil be runnable by a simple 
`docker-compose up -d` command.

A mobile app using Flutter may also be developed if time allows.

Written by Michael Lee (michaellee8). Licensed in MIT.