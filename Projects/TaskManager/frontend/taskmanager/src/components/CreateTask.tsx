// Alex Miller
// component for creating tasks

import { useEffect, useState } from "react";
import { createItem } from "../api/axios";
import type { Item } from "../types/Item";
import Trashcan from "./Trashcan";

type Props = {
    onCreate: (newItem: Item) => void;
}

const CreateTask: React.FC<Props> = ({ onCreate }) => {


    const [formdata, setFormdata] = useState({ title: '', description: ''});

    {/* add a task to the list */}
    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        const newItem = {title: formdata.title, description: formdata.description, container: 'ToDo'};
        const res = await createItem(newItem);
        onCreate(res.data);
        setFormdata({ title: '', description: '' });
    }

    return (
        <div className="">

            {/* title section */}
            <section>
                <h1 className="text-lg">Create Tasks</h1>
            </section>

            {/* form section */}
            <section className="py-5 flex flex-row justify-center items-center">
                <form onSubmit={handleSubmit} className="flex flex-row text-center justify-center items-center">

                    {/* title */}
                    <label className="px-10">Title</label>
                    <input
                        placeholder="Title"
                        type="text"
                        required
                        value={formdata.title}
                        onChange={(e) => setFormdata({ ...formdata, title: e.target.value })}
                        className="border border-white px-2 rounded focus:outline-none focus:ring-3 focus:ring-blue-600 focus:border-black"
                    />

                    {/* description */}
                    <label className="px-10">Description</label>
                    <input
                        placeholder="description"
                        type="text"
                        required
                        value={formdata.description}
                        onChange={(e) => setFormdata({ ...formdata, description: e.target.value })}
                        className="border border-white px-2 rounded focus:outline-none focus:ring-3 focus:ring-blue-600 focus:border-black"
                    />

                    <div className="px-10">
                        <button 
                            type="submit" 
                            className="
                                bg-green-500 
                                text-black 
                                text-xl 
                                px-3
                                py-2
                                font-bold
                                rounded
                                hover:ring-4
                                hover:ring-green-700
                            "
                        >
                            ADD
                        </button>
                    </div>
                </form>
                <Trashcan />
            </section>
        </div>
    )
}

export default CreateTask;

