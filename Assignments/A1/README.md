<!--- The following README.md sample file was adapted from https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#file-readme-template-md by Gabriella Mosquera for academic use --->
<!--- You may delete any comments in this sample README.md file. If needing to use as a .txt file then simply delete all comments, edit as needed, and save as a README.txt file --->

# Assignment 1 (Individual)

For this assignment 1 I have worked on the comment system feature.
My prototype has been implemented for submitting and deleting a comment.

- _Date Created_: 06 June 2024
- _Last Modification Date_: 07 June 2024
- _Hosted Assignment 1 URL_: <https://samshada1.netlify.app/>
- _Gitlab Assignment Repository URL_: <https://git.cs.dal.ca/msrahman/csci-5709-assignments>

## Authors

- Md Samshad Rahman (samshad@dal.ca) - (B00968344)

## Getting Started

### Prerequisites

To have a local copy of this assignment up and running on local machine, first need to install the following libraries

```
- [Node.js](https://nodejs.org/) (version 18.x or later)
- [Yarn](https://yarnpkg.com/) (version 1.22.x or later)
```

See the following section for detailed step-by-step instructions on how to run the project on a local machine.

### Installing

1. `yarn` to install npm packages
2. `yarn start` to start dev server

## Deployment

I have pushed the code to my GitHub private repository. Then I logged into Netlify and connected my GitHub repository to Netlify. I have deployed the code to Netlify by selecting the repository and "yarn build" - build command.

## Built With

<!--- Provide a list of the frameworks used to build this application, your list should include the name of the framework used, the url where the framework is available for download and what the framework was used for, see the example below --->

- [React](https://legacy.reactjs.org/docs/getting-started.html/) - The web framework used
- [npm](https://docs.npmjs.com//) - Dependency Management
- [Yarn](https://yarnpkg.com/) - Dependency Management
- [Netlify](https://www.netlify.com/) - Deployment

## Sources Used

For the design elements and structures inspired by various well-known websites, including Facebook, Reddit, and an open-source templates on Figma. These sources provided a foundation for the layout, user interface, and interaction elements, ensuring familiarity and user-friendly navigation.

### Templates

- [interactive-comments-section](https://www.figma.com/community/file/1092016656607907112/interactive-comments-section) - For the design idea of the comment section
- [Facebook Comments Plugin](https://www.figma.com/community/file/1110976092414948047/facebook-comments-plugin) - For the button design idea (Reply, Edit, Delete) of the comment section
- [Reddit post comment](https://www.figma.com/community/file/1379250773400483815/reddit-post-comment) - For the design idea for voting system in comment section

## Artificial Intelligence Tools Used

I have used OpenAI's ChatGPT to generate project structure and CSS code for the comment system feature. The AI tool was used to generate structures, which were then modified and implemented in the project.

- [ChatGPT-4.0](https://chatgpt.com/) - The AI Tool used

### Prompt Used on _ChatGPT_

```
I've attached a figma in PDF format.

I'll create this project with react,
can you provide a rough project structure ideas including css
and also provide some references as well for the design.
```

Generated reply:

```
Based on the PDF design you provided, it appears to be a commenting system or discussion board interface. Here’s a rough project structure and some initial code for building this project with React.

Project Structure
java
Copy code
my-app/
├── public/
│   ├── index.html
│   └── ...
├── src/
│   ├── components/
│   │   ├── Comment.js
│   │   ├── CommentList.js
│   │   ├── CommentForm.js
│   │   ├── CommentReply.js
│   │   └── ...
│   ├── styles/
│   │   ├── App.css
│   │   ├── Comment.css
│   │   ├── CommentList.css
│   │   └── ...
│   ├── App.js
│   ├── index.js
│   └── ...
├── package.json
└── ...
Basic React Components
1. App.js
jsx
Copy code
import React from 'react';
import CommentList from './components/CommentList';
import './styles/App.css';

function App() {
  return (
    <div className="App">
      <h1>Discussion Board</h1>
      <CommentList />
    </div>
  );
}

export default App;
2. CommentList.js
jsx
Copy code
import React, { useState } from 'react';
import Comment from './Comment';
import CommentForm from './CommentForm';
import './CommentList.css';

const CommentList = () => {
  const [comments, setComments] = useState([]);

  const addComment = (text) => {
    setComments([...comments, { text, replies: [] }]);
  };

  const addReply = (index, replyText) => {
    const newComments = [...comments];
    newComments[index].replies.push(replyText);
    setComments(newComments);
  };

  return (
    <div className="comment-list">
      <CommentForm addComment={addComment} />
      {comments.map((comment, index) => (
        <Comment key={index} comment={comment} addReply={(replyText) => addReply(index, replyText)} />
      ))}
    </div>
  );
};

export default CommentList;
3. Comment.js
jsx
Copy code
import React, { useState } from 'react';
import CommentReply from './CommentReply';
import './Comment.css';

const Comment = ({ comment, addReply }) => {
  const [showReplyForm, setShowReplyForm] = useState(false);

  return (
    <div className="comment">
      <p>{comment.text}</p>
      <button onClick={() => setShowReplyForm(!showReplyForm)}>Reply</button>
      {showReplyForm && <CommentReply addReply={addReply} />}
      {comment.replies.map((reply, index) => (
        <div key={index} className="reply">{reply}</div>
      ))}
    </div>
  );
};

export default Comment;
4. CommentForm.js
jsx
Copy code
import React, { useState } from 'react';
import './CommentForm.css';

const CommentForm = ({ addComment }) => {
  const [text, setText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    addComment(text);
    setText('');
  };

  return (
    <form onSubmit={handleSubmit} className="comment-form">
      <textarea value={text} onChange={(e) => setText(e.target.value)} placeholder="Add a comment..." />
      <button type="submit">Post Comment</button>
    </form>
  );
};

export default CommentForm;
5. CommentReply.js
jsx
Copy code
import React, { useState } from 'react';
import './CommentReply.css';

const CommentReply = ({ addReply }) => {
  const [text, setText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    addReply(text);
    setText('');
  };

  return (
    <form onSubmit={handleSubmit} className="comment-reply-form">
      <textarea value={text} onChange={(e) => setText(e.target.value)} placeholder="Add a reply..." />
      <button type="submit">Post Reply</button>
    </form>
  );
};

export default CommentReply;
Basic CSS Styles
App.css
css
Copy code
.App {
  font-family: Arial, sans-serif;
  margin: 20px;
}

h1 {
  text-align: center;
}
CommentList.css
css
Copy code
.comment-list {
  max-width: 600px;
  margin: 0 auto;
}
Comment.css
css
Copy code
.comment {
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 10px;
}

.reply {
  margin-left: 20px;
  padding: 5px;
  border-left: 2px solid #ccc;
}
CommentForm.css
css
Copy code
.comment-form {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
}

.comment-form textarea {
  resize: none;
  padding: 10px;
  margin-bottom: 10px;
}

.comment-form button {
  align-self: flex-end;
}
CommentReply.css
css
Copy code
.comment-reply-form {
  display: flex;
  flex-direction: column;
  margin-top: 10px;
}

.comment-reply-form textarea {
  resize: none;
  padding: 10px;
  margin-bottom: 10px;
}

.comment-reply-form button {
  align-self: flex-end;
}
References
React Documentation
CSS Tricks
MDN Web Docs
This structure and code should give you a good starting point to build your project. Adjustments will be necessary depending on your specific requirements and the details from your design.

```

### Prompt Used on _ChatGPT_

```
<svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M16 14L12 10L8 14" stroke="#200E32" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>

make this svg upside down

```

Generated reply:

```
To flip the SVG upside down, you can use a transformation. Specifically, you can apply a rotation transformation to rotate the SVG by 180 degrees around its center. Here's the modified SVG code:

xml
Copy code
<svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <g transform="rotate(180, 12, 12)">
    <path d="M16 14L12 10L8 14" stroke="#200E32" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
</svg>
Explanation:
The g element is a grouping element in SVG, which allows us to apply transformations to a group of SVG elements.
The transform="rotate(180, 12, 12)" attribute rotates the group by 180 degrees around the point (12, 12), which is the center of the viewBox (since the viewBox is 24x24). This effectively flips the SVG upside down.

```

#### File Name

_src/images/icon-plus.svg_

- <!---How---> The code in [src/images/icon-plus.svg] was implemented by ChatGPT generated code.
- <!---Why---> [src/images/icon-plus.svg]'s Code was used because I was unable to find similar down arrow SVG.
- <!---How---> [src/images/icon-plus.svg]'s I asked ChatGPT to flip the SVG upside down.

## Acknowledgments

- [interactive-comments-section](https://www.figma.com/community/file/1092016656607907112/interactive-comments-section)
- [Facebook Comments Plugin](https://www.figma.com/community/file/1110976092414948047/facebook-comments-plugin)
- [Reddit post comment](https://www.figma.com/community/file/1379250773400483815/reddit-post-comment)
