import React from 'react';

export default function Search() {
  return (
    <div>

      <div>
      <h3 className='text-2xl text-white font-bold tracking-tight mb-4'>All categories</h3>
      <div className='grid grid-cols-5 gap-5'>
      {new Array(40).fill(
              <a className='overflow-hidden' href="#" >
                <div className='bg-purplebox h-[220px] rounded-lg p-4 relative'>
                    <span className='text-4xl font-bold'>Pop</span>
                    <img className='w-[108px] h-[108px] -right-5 bottom-0 absolute rotate-25 shadow-2xl'  src="https://t.scdn.co/images/0a74d96e091a495bb09c0d83210910c3" />
                </div>
              </a>
      )}
      </div>
      </div>
    </div>
  )
}