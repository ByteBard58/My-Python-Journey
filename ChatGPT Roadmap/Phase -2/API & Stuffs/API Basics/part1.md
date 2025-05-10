# All About API

## This is my note of this [video](https://youtu.be/WXsD0ZgxjRw?si=-SDLvOdFl4UIxqZx) which I watched to cover the basics of API

---

### Part -1: The Introduction

**API = Application Programming Interface**

- First of all, what does **Interface** mean?

Interface is the front-end part which a regular user sees and interacts with while having no idea how this stuff works.

- Now, let's dive into API:

API is a set of code that packs a certain functionality, allowing the developer to do more without writing extra code.

API helps us avoid writing **EVERYTHING** from scratch. It allows us to integrate more features by reusing existing code.

---

### Part -2: Remote API

A Remote API is a kind of API that works over the internet. It's not limited to your device — it can be accessed from anywhere, anytime.

There are many types of Remote APIs. The most popular one is **REST** (Representational State Transfer).

REST defines a set of rules for building APIs. APIs that follow these rules are called **RESTful APIs**. REST uses HTTP methods to connect clients with servers and vice versa.

Other types of APIs include:
1. GraphQL
2. SOAP
3. WebSockets
...and more.

---

### Part -3: How the Web Works

When loading a website:

- Our browser → The **Client**
- The client sends a **request** to get the data of a certain website from the server.
- The server identifies the requested website via the **URL** (Uniform Resource Locator) or **URI** (Uniform Resource Identifier).
- The server sends the data back to the client — this is called a **response**.

During this request-response cycle, a set of rules is followed called **HTTP** (Hypertext Transfer Protocol). HTTP has some key methods used to send requests:

- **GET** → Fetches data from the server (like reading a file).
- **POST** → Sends new data to the server to create something (like submitting a form).
- **PUT** → Updates or replaces existing data on the server (like overwriting a file).
- **DELETE** → Removes data from the server (like deleting a file).

**S.N:** People nowadays often use POST a lot more than PUT. In this way, they create more versions of the same code without actually **updating** them.

Also, the responses include **status codes**, which show the result of the request:

- **2XX** → Success  
- **3XX** → Redirection (Additional step required)  
- **4XX** → Client-side Error  
- **5XX** → Server-side Error  

One important fact: **HTTP is stateless** — it doesn’t remember anything after the request-response cycle is done.

---

### Part -4: RESTful API Constraint Scavenger Hunt

- So, what is a RESTful API?

A **RESTful API** is an API that follows the constraints (rules) of REST. In simple terms, if an API follows the rules of REST, it's RESTful.

Now let’s list the **constraints** (rules) of REST:

1. Client-Server Architecture  
2. Statelessness  
3. Cacheability  
4. Layered System  
5. Code on Demand  
6. Uniform Interface  

We're not going to be dumb enough to learn **all** of these at once — we’ll cover them as we go. Points 1 and 2 are already explained in the earlier section.

---
### Part -5: Exploring an API online

Just like Craig, I also played with the spotify API in their [website](https://developer.spotify.com/documentation/web-api). I cant just share all the experience on words, but here's what's important;

When we saw the list of constraints of REST API, there was one named **Layered System**. In the spotify API, the responses were being returned in a very layered system. Every option (artist, album, genre etc.) returned the specific JSON data. So we can say that, RESTful APIs follow a very structured and layered system.
--
*Unfinished*