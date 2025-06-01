// Alex Miller
// Task Manager application

import './App.css';
import { useState, useEffect } from 'react';
import type { Item } from './types/Item';
import CreateTask from './components/CreateTask';
import TaskContainer from './components/TaskContainer';
import { DndContext, DragOverlay } from '@dnd-kit/core';
import type { DragEndEvent } from '@dnd-kit/core';
import { deleteItem, updateItem, getItems } from './api/axios';

function App() {

  const [items, setItems] = useState<Item[]>([]);
  const [activeItem, setActiveItem] = useState<Item | null>(null);


  useEffect(() => {
    const fetchItems = async () => {
      try {
        const items = await getItems();
        setItems(items.data);
      }
      catch (error) {
        console.error('Error getting items: ', error);
      }
    }

    fetchItems();
  }, []);


  // handle the end of the drag
  const hangleDragEnd = async (event: DragEndEvent) => {
    const { active, over } = event;
    const draggedItem = active.data.current?.item as Item;

    if (!draggedItem) return;
    

    if (over) {
      const newContainer = over.id as string;

      // deletion
      if (over.id === 'trash') {
        setItems(prev => prev.filter(i => i.id !== draggedItem.id));

        deleteItem(draggedItem.id).catch(error => {
          console.error('Failed to delete item: ', error);
        });
      }

      // move
      else if (draggedItem.container !== newContainer) {
        setItems(prev =>
          prev.map(item => 
            item.id === draggedItem.id
            ? { ...item, container: newContainer }
            : item
          )
        );

        updateItem(draggedItem.id, {
          title: draggedItem.title,
          description: draggedItem.description,
          container: newContainer
        }).catch(error => {
          console.error('Failed to update item: ', error);
        })
      }
    }

    setActiveItem(null);
  };

  return (
    <DndContext 
      onDragEnd={hangleDragEnd}
      onDragStart={(event) => {
        const item = event.active.data.current?.item as Item;
        setActiveItem(item);
      }}
    >
      <div className="flex flex-row">
        <main className="text-white w-screen h-screen bg-gray-900 text-center">

          {/* create tasks */}
          <section className="py-10 bg-black">
            <CreateTask 
              onCreate={(item) => setItems(prev => [...prev, item])}
            />
          </section>
          
          {/* each container */}
          <section className="py-20 flex flex-row justify-center items-center">

            {/* ToDo */}
            <div className="w-1/3 px-10">
              <TaskContainer 
                title="ToDo"
                containerId="ToDo"
                items={items.filter(i => i.container === 'ToDo')}
                color="bg-red-500 border-solid border border-red-500"
              />
            </div>

            {/* InProgress */}
            <div className="w-1/3 px-10">
              <TaskContainer 
                title="In Progress"
                containerId="IP"
                items={items.filter(i => i.container === "IP")}
                color="bg-yellow-500 border-solid border border-yellow-500"
              />
            </div>

            {/* Done */}
            <div className="w-1/3 px-10">
              <TaskContainer 
                title="Done"
                containerId="Done"
                items={items.filter(i => i.container === "Done")}
                color="bg-green-500 border-solid border border-green-500"
              />
            </div>

          </section>
        
        </main>
      </div>

      {/* overlay for dragging, no z coord issues */}
      <DragOverlay>
        {activeItem ? (
          <div className="bg-gray-900 m-2 px-2 cursor-move text-white w-full">
            <div className="text-lg font-bold">{activeItem.title}</div>
            <div className="text-sm font-semibold text-gray-400">
              {activeItem.description}
            </div>
          </div>
        ) : null}
      </DragOverlay>

    </DndContext>
    
  );
}

export default App;
